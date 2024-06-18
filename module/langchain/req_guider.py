import json
from langchain import LLMChain, PromptTemplate
from .chain import llm

# guide_prompt = """
#     {req}
#     Decompose user requirements into smaller sub-requirements.no more than 4 steps.each step no more than 10 words"""
guide_prompt = """
    {req}
    Decompose user requirements into 3 sub-requirements. Each step, maximum 10 words.do not need test and validiation."""
req_prompt_template = PromptTemplate(
    input_variables=["req"],
    template=guide_prompt,
)
req_chain = LLMChain(llm=llm, prompt=req_prompt_template)
if __name__ == "__main__":
    
    print(req_chain.run(req=
                       """implementing the addition of a new employee functionality within the Spring framework across the controller, service, and mapper."""))
