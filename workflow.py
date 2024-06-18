import os
import subprocess
from git import Repo
import json
import faiss
import numpy as np
import tqdm
from module.embedding import index_texts_with_sbert, encode_text, load_sbert_model
from module.langchain.file2description import analyze_chain
from module.langchain.req_guider import req_chain
from module.langchain.code_generator_fromdoc import code_chain
from module.langchain.document_generator import document_chain
from module.langchain.codecheck import check_chain
from module.langchain.candidateFilter import candidate_chain
from module.langchain.attr_refine import attr_chain
from module.parser.my_parser import parser
from module.langchain.file2nl import nl_chain
from collections import Counter

def fileDescriptionFaiss(projectname,filepath, extension,task):
    func_require = {}
    attr_require = {}
    for root, dirs, files in os.walk(filepath):
        for f in files:
            if any(f.endswith(ext) for ext in extension):
                relpath = os.path.relpath(root, filepath)
                normpath = relpath.replace('\\','/')
                fileAddr = '{}/{}/{}'.format(filepath,normpath, f)
                method, nl , attribute= antlrInit(projectname,fileAddr,f)
                for i, j in zip(method, nl):
                    if j != "null":
                        file_method = f + " " + i
                        # print(file_method)
                        # print(j)
                        func_require.update({j: file_method})
                # if len(attribute) > 0 and (len(attribute)>len(method)) :
                if len(attribute) > 0:
                    # print(attribute)
                    attr_require.update({','.join(attribute): f})
    faiss_store_func = list(func_require.keys())
    faiss_store_attr = list(attr_require.keys())
    model_name = "multi-qa-mpnet-base-cos-v1"
    # print(len(faiss_store_func))
    # print(len(faiss_store_attr))
    if(len(faiss_store_func) > 0):
        index_texts_with_sbert(faiss_store_func, model_name , path="database/{}/method_{}.index".format(projectname,task))
    else:
        with open("database/{}/method_{}.index".format(projectname,task), 'w', encoding='utf-8') as f:
            json.dump({}, f)
    if(len(faiss_store_attr) > 0):
        index_texts_with_sbert(faiss_store_attr, model_name, path="database/{}/attr_{}.index".format(projectname,task))
    else:
        with open("database/{}/attr_{}.index".format(projectname,task), 'w', encoding='utf-8') as f:
            json.dump({}, f)
    with open("database/{}/nl2method_{}.json".format(projectname,task), "w", encoding='utf-8') as f:  ## 设置'utf-8'编码
        f.write(json.dumps(func_require, ensure_ascii=False, indent=4))
    with open("database/{}/attr2method_{}.json".format(projectname,task), "w", encoding='utf-8') as f:  ## 设置'utf-8'编码
        f.write(json.dumps(attr_require, ensure_ascii=False, indent=4))


def buildFaissIndex(projectname,folder_path, file_extension, gitbranch):
    # folder_path = '../sky-take-out'
    # file_extension = ['.java']
    fileDescriptionFaiss(projectname,folder_path, file_extension, gitbranch)


def candidateSearch(requirement,dict, faiss_index, topk=5):
    # print(faiss_index.ntotal)
    requirement_embedding = encode_text([requirement],"multi-qa-mpnet-base-cos-v1")
    # print(faiss_index.search(np.expand_dims(requirement_embedding, axis=0),10))
    distances, indices = faiss_index.search(requirement_embedding, topk)
    candidate = []
    texts = list(dict.items())
    # 这里是取出来的topk候选集
    # print(requirement)
    for i in range(len(indices[0])):
        text = texts[indices[0][i]]
        candidate.append(text)
        # print(f'Top {i + 1}: {text}, Distance: {distances[0][i]}')
    # 这里是候选集的gpt处理
    # candidate_list = candidate_chain.run({'requirement': requirement, 'candidate': ' '.join(candidate)}).split(" ")
    # print(candidate_list)
    return candidate


def antlrInit(projectname,fileaddr,f):
    print(fileaddr)
    print(f)
    nl_list = []
    attribute = []
    method = []
    json_path = "database/{}/gptCache.json".format(projectname)
    if not os.path.exists(json_path):
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump({}, f)
    nl_cache = json.load(open(json_path))
    modify = False

    # attribute, method, body = parser(fileaddr)
    # python太慢了，用java做
    # attribute, method, body = parser(fileaddr)
    antlr_command = "java -jar module/parser/MyAntlr.jar {}".format(fileaddr)
    process = subprocess.Popen(antlr_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return_code = process.wait()
    # if(return_code != 0):
    #     print("Antlr Error")
    #     return
    # else:
    #     print("Antlr Success")
    result = json.load(open("list.json",encoding='utf-8'))
    attribute = result[0]
    method = result[1]
    body = result[2]
    for i, j in zip(method, body):
        if j == "; " or j == "{} ":
            nl_list.append("null")
        elif nl_cache.get(str(f) + " "+ i) is not None:
            # print("hit")
            nl_list.append(nl_cache.get(f + " "+ i))
        else:
            modify = True
            # print("miss")
            nl = nl_chain.run(i + '\n' + j)
            nl_list.append(nl)
            nl_cache.update({str(f)+" "+i: nl})
    if modify:
        with open(json_path, "w", encoding='utf-8') as f:  ## 设置'utf-8'编码
            f.write(json.dumps(nl_cache, ensure_ascii=False, indent=4))
    # print(len(nl_list), "             ",len(method))
    # print("method :", method)
    # print("nl :", nl_list)
    # print("attribute :", attribute)
    return method, nl_list, attribute


# def antlrSearch(candidate_list, file_dict):
#     description_list = []
#     for i in candidate_list:
#         if i.startswith('\n'):
#             i = i.replace('\n', '')
#         try:
#             # print(file_dict[i])
#             # print("../sky-take-out/{}".format(file_dict[i]))
#             attribute, method = parser("../sky-take-out/{}".format(file_dict[i]))
#             description_list.append("\n\n Exists_file: " + i)
#             if len(attribute) > 0:
#                 description_list.append("\n Attribute: " + ' '.join(attribute))
#             if len(method) > 0:
#                 description_list.append("\n Method: " + ' '.join(method))
#             # print(attribute)
#             # print(method)
#         except:
#             print("file not found")
#             continue
#         finally:
#             print("file read success")
#         # print(description_list)
#         # print(" ".join(description_list))
#     return " ".join(description_list)


# def descriptionSearch(candidate_list, file_dict):
#     description_list = []
#     for i in candidate_list:
#         if i.startswith('\n'):
#             i = i.replace('\n', '')
#         try:
#             with open("../sky-take-out/{}".format(file_dict[i]), 'r', encoding='utf-8') as f:
#                 content = f.read()
#                 res = analyze_chain.run(content)
#                 description_list.append(res)
#                 print(f.read())
#                 print(res)
#         except:
#             print("file not found")
#             continue
#         finally:
#             print("file read success")
#     return description_list


def documentGenerator(requirement, func_list, entity_list):
    description = ""
    description += "Function: " + "\n"
    for i in func_list:
        description += i[1] + ":" + i[0] + "\n"
    description += "Entity: " + "\n"
    for i in entity_list:
        description += i[1] + ":" + i[0] + "\n"
    # print(description)
    document = document_chain.run({'requirement': requirement, 'abstract': description})
    return document

def refineGenerator(requirement, func_list, entity_list):
    description = ""
    description += "Function: " + "\n"
    for i in func_list:
        description += i[1] + ":" + i[0] + "\n"
    description += "Entity: " + "\n"
    for i in entity_list:
        description += i[1] + ":" + i[0] + "\n"
    # print(description)
    document = document_chain.run({'requirement': requirement, 'abstract': description})
    return document


def codeGeneration(document):
    code = code_chain.run({'document': document})
    return code




def refine_requirement(requirement):
    refine_req = req_chain.run({'req': requirement})
    # print(refine_req)
    return refine_req.split("\n")

def workflow(projectname,projectbase,gitbranch, requirement):
    previous_directory = os.getcwd()
    repo = Repo(projectbase)
    os.chdir(projectbase)
    # print(os.getcwd())
    # print(repo.active_branch.name)
    target_branch = gitbranch
    repo.git.checkout(target_branch)
    print(repo.active_branch.name)
    os.chdir(previous_directory)
    # print(os.getcwd())
    buildFaissIndex(projectname,projectbase, ['.java'], gitbranch)
    # ---refine---: step by step
    refine_req = refine_requirement(requirement)
    func_dict = json.load(open("database/{}/nl2method_{}.json".format(projectname,gitbranch),encoding='utf-8'))
    attr_dict = json.load(open("database/{}/attr2method_{}.json".format(projectname,gitbranch),encoding='utf-8'))
    # file_name = list(file_dict.keys())
    if func_dict != {}:
        faiss_index_func = faiss.read_index("database/{}/method_{}.index".format(projectname,gitbranch))
    else:
        faiss_index_func = None
    if attr_dict != {}:
        faiss_index_attr = faiss.read_index("database/{}/attr_{}.index".format(projectname,gitbranch))
    else:
        faiss_index_attr = None
    #
    func_list = []
    entity_list = []
    k = 6

    for step in refine_req:
        if faiss_index_func != None:
            func_list += candidateSearch(step,func_dict,faiss_index_func,k)
        if faiss_index_attr != None:
            entity_list += candidateSearch(step, attr_dict, faiss_index_attr,k)
    # entity_req = attr_chain.run(requirement + " " + refine_req[0])
    # entity_list = candidateSearch(requirement, attr_dict, faiss_index_attr, k)
    refine_req.insert(0,requirement)
    # refine_req.append(entity_req)
    
    # func_list_uniq = list(set(func_list))
    # entity_list_uniq = list(set(entity_list))
    if faiss_index_func != None:
        func_list_counter = Counter(func_list)
        func_list_top = func_list_counter.most_common(5)
        func_list_uniq  = [item[0] for item in func_list_top]
    else:
        func_list_uniq = []
    if faiss_index_attr != None:
        entity_list_counter = Counter(entity_list)
        entity_list_top = entity_list_counter.most_common(5)
        entity_list_uniq  = [item[0] for item in entity_list_top]
    else:
        entity_list_uniq = []
    # entity_list_uniq = entity_list
    # func_list_uniq = list(set([x for x in func_list if func_list.count(x) > 1]))
    # entity_list_uniq = list(set([x for x in entity_list if entity_list.count(x) > 1]))
    document = documentGenerator(refine_req, func_list_uniq, entity_list_uniq)
    code = codeGeneration(document)
    checkcode = check_chain.run({'code': code})
    candidate = []
    for i in func_list_uniq:
        candidate.append(i[1])
    if faiss_index_attr != None:
        for i in entity_list_uniq:
            candidate.append(i[1])
    return refine_req,candidate,document,code,checkcode



if __name__ == "__main__":
    # requirement = "implementing the addition of a new employee functionality within the Spring framework, employee have id, name,phone, and age."
    # previous_directory = os.getcwd()
    projectname = 'jgrapht'  
    projectbase = 'project/{}'.format(projectname)
    req_dict = json.load(open("test/{}/requirement.json".format(projectname)))
    for task in req_dict:
        requirement = req_dict[task]
        refine_req,candidate,document,code,checkcode = workflow(projectname,projectbase,task, requirement)
        fw = open("test/{}/{}.txt".format(projectname,task), 'w') 
        fw.write("\n".join(refine_req))  
        fw.write("\n")  
        fw.write("\n".join(candidate))
        fw.write("\n")    
        fw.write("".join(document))
        fw.write("\n")    
        fw.write(code)
        fw.write("----------------------------------------")
        fw.write("\n")
        fw.write(checkcode)
        fw.close()