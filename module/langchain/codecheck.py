import json
from langchain import LLMChain, PromptTemplate
from .chain import llm

check_prompt = """
    Supplement existing Java code based on the description, do not generate new function. 
    {code}
    """
check_prompt_template = PromptTemplate(
    input_variables=["code"],
    template=check_prompt,
)
check_chain = LLMChain(llm=llm, prompt=check_prompt_template)
