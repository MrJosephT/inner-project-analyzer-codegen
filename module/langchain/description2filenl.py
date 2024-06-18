from langchain import LLMChain, PromptTemplate
from .chain import llm

analyze_prompt = """ Compiles interface documentation from a specified code file to produce a succinct summary of its functionality. Generates a concise yet comprehensive description of the code's overall purpose, utilizing fewer than two sentences to encapsulate its primary function.

{requirement}
I think this file mostly :"""
analyze_prompt_template = PromptTemplate(
    input_variables=["requirement"],
    template=analyze_prompt,
)
analyze_chain = LLMChain(llm=llm, prompt=analyze_prompt_template)
print(analyze_chain.run("""
Function Name: save
Input Parameters: CategoryDTO
Output Parameters: Result<String>
Description: This function is used to create a new category. It takes a CategoryDTO object as an input parameter and returns a Result<String> object as an output parameter.

Function Name: page
Input Parameters: CategoryPageQueryDTO
Output Parameters: Result<PageResult>
Description: This function is used to query a page of categories. It takes a CategoryPageQueryDTO object as an input parameter and returns a Result<PageResult> object as an output parameter.

Function Name: deleteById
Input Parameters: Long id
Output Parameters: Result<String>
Description: This function is used to delete a category by its id. It takes a Long id as an input parameter and returns a Result<String> object as an output parameter.

Function Name: update
Input Parameters: CategoryDTO
Output Parameters: Result<String>
Description: This function is used to update a category. It takes a CategoryDTO object as an input parameter and returns a Result<String> object as an output parameter.

Function Name: startOrStop
Input Parameters: Integer status, Long id
Output Parameters: Result<String>
Description: This function is used to enable or disable a category. It takes an Integer status and a Long id as input parameters and returns a Result<String> object as an output parameter.

Function Name: list
Input Parameters: Integer type
Output Parameters: Result<List<Category>>
Description: This function is used to query a list of categories by type. It takes an Integer type as an input parameter and returns a Result<List<Category>> object as an output parameter.
"""))