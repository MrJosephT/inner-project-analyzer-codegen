from langchain import LLMChain, PromptTemplate
from .chain import llm

document_prompt = """
Compose a development document according to requirement and existing file_description.Do not generate existing function or entity.
Do not generate existing function or entity.
You can generate multiple functions in a single document.
requirement: {requirement}
file_description: {abstract}
'''
template:
Function Header: {{Function Header with signature}}

Description:
{{Describe the functionality, purpose, and implementation of the function here,no more than 20 words.}}

Reuse Functions or Entities:
{{List all functions and entities required as per the file_description. }}
...

Parameters:
{{Parameter}}: {{Description of parameter}}
...

Return Value:
{{Focus on determining if existing descriptions include usable return values.}}

'''
"""
# document_prompt = """
# Compose a development document according to requirement and existing file_description.Do not generate existing function or entity.
# Do not generate existing function or entity.
# You can generate multiple functions in a single document.
# requirement: {requirement}
# file_description: {abstract}
# template:
# ///
# Function Header: {{Function Header with signature}}

# Description:
# {{Describe the functionality, purpose, and implementation of the function here,no more than 20 words.}}

# Reuse Functions or Entities:
# {{List all functions and entities required as per the file_description. }}
# ...

# Parameters:
# {{Parameter}}: {{Description of parameter}}
# ...

# Return Value:
# {{Focus on determining if existing descriptions include usable return values.}}
# ///
# """
# document_prompt = """Compose a development document using existing project data, minimizing code development, and optimizing codebase utilization for user requirements.Specify the method's signature, description, and provide steps for method.
# requirement: {requirement}
# Note: Document should not contain file in Exists_file.
# exists_file_abstracts:' {abstract} '
# template:
# 'Method Signature:
# public static Long getId(int id)
# ...'
# """
document_prompt_template = PromptTemplate(
    input_variables=["requirement","abstract"],
    template=document_prompt,
)
document_chain = LLMChain(llm=llm, prompt=document_prompt_template)
if __name__ == "__main__":
    pass