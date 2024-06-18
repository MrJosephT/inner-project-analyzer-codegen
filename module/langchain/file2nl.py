import json
from langchain import LLMChain, PromptTemplate
from .chain import llm

nl_prompt = """
    {method}
    Summarize function role and description within project context no more than 20 words:"""
nl_prompt_template = PromptTemplate(
    input_variables=["method"],
    template=nl_prompt,
)
nl_chain = LLMChain(llm=llm, prompt=nl_prompt_template)
if __name__ == "__main__":
    print(nl_chain.run(method=
                       """
                       Result<EmployeeLoginVO> login(@RequestBodyEmployeeLoginDTOemployeeLoginDTO) 
{log.info("员工登录：{}",employeeLoginDTO);Employeeemployee=employeeService.login(employeeLoginDTO);Map<String,Object>claims=newHashMap<>();claims.put(JwtClaimsConstant.EMP_ID,employee.getId());Stringtoken=JwtUtil.createJWT(jwtProperties.getAdminSecretKey(),jwtProperties.getAdminTtl(),claims);EmployeeLoginVOemployeeLoginVO=EmployeeLoginVO.builder().id(employee.getId()).userName(employee.getUsername()).name(employee.getName()).token(token).build();returnResult.success(employeeLoginVO);} 
"""))
