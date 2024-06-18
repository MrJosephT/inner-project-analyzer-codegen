import json
from langchain import LLMChain, PromptTemplate
from .chain import llm

code_prompt = """Develop code by interpreting user requirements. Ensure the generated code adheres to the project's specified requirements, emphasizing effectiveness, readability, and adherence to best practices.
requirement: {requirement}
develope_code:"""
code_prompt_template = PromptTemplate(
    input_variables=["requirement"],
    template=code_prompt,
)
code_chain = LLMChain(llm=llm, prompt=code_prompt_template)
if __name__ == "__main__":
    file_dict = json.load(open("../../test/testfile.json"))
    file_name = list(file_dict.keys())
    for i in file_name:
        with open("./test/gpt_tester/{}.txt".format(i),"w", encoding='utf-8') as f:
            ans = code_chain(file_dict[i])
            print(ans)
            f.write(ans['text'])    