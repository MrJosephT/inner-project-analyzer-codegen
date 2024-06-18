from langchain import LLMChain, PromptTemplate
from .chain import llm

candidate_prompt = """Given a list of filenames and user requirements, identify the files that are pertinent to the user's needs and make the corresponding selections.
            template:candidate1 candidate2 candidate3 ...
            requirement: {requirement}
            candidate: {candidate}
            """
candidate_prompt_template = PromptTemplate(
    input_variables=["requirement", "candidate"],
    template=candidate_prompt,
)
candidate_chain = LLMChain(llm=llm, prompt=candidate_prompt_template)
