import json
import subprocess

antlr_command = "java -jar module/parser/MyAntlr.jar {}".format("project/sky-take-out/sky-common/src/main/java/com/sky/constant/AutoFillConstant.java")

process = subprocess.Popen(antlr_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

result = json.load(open("list.json"))
print(result[0])
print(type(result[0]))