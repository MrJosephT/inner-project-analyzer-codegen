from langchain import LLMChain, PromptTemplate
from chain import llm
# code_prompt = """Develop code by interpreting user requirements and leveraging existing project information. Ensure the generated code adheres to the project's specified requirements, emphasizing effectiveness, readability, and adherence to best practices.
# requirement: {requirement}
# Note: don't generate code that described in Exists_file and Method, only generate code that is relevant to the user's requirements description.
# exists_file_abstracts: {abstract}
# develope_code:"""
code_prompt = """Generate Java code precisely as per requirement, excluding descriptions.
Do not generate descriptions, only generate code.
requirement: {requirement}
Write your code here:"""
code_prompt_template = PromptTemplate(
    input_variables=["requirement"],
    template=code_prompt,
)
code_chain = LLMChain(llm=llm, prompt=code_prompt_template)
