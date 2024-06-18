from langchain import LLMChain, PromptTemplate
from .chain import llm

attr_prompt = """Identify key attributes and objects for the requirements.
            requirements: {requirement}
            template:
'attribute1 attribute2 attribute3 ...'
            """
attr_prompt_template = PromptTemplate(
    input_variables=["requirement"],
    template=attr_prompt,
)
attr_chain = LLMChain(llm=llm, prompt=attr_prompt_template)
