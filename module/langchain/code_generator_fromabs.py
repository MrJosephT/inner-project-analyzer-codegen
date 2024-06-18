from langchain import LLMChain, PromptTemplate
from .chain import llm
# code_prompt = """Develop code by interpreting user requirements and leveraging existing project information. Ensure the generated code adheres to the project's specified requirements, emphasizing effectiveness, readability, and adherence to best practices.
# requirement: {requirement}
# Note: don't generate code that described in Exists_file and Method, only generate code that is relevant to the user's requirements description.
# exists_file_abstracts: {abstract}
# develope_code:"""
code_prompt = """Develop code by interpreting user requirements and leveraging existing project information. Ensure the generated code adheres to the project's specified requirements, emphasizing effectiveness, readability, and adherence to best practices.
requirement: {requirement}
Note: don't generate code that described in Exists_file and Method, only generate code that is relevant to the user's requirements description.
exists_file_abstracts: {abstract}
Generate_code:"""
code_prompt_template = PromptTemplate(
    input_variables=["requirement","abstract"],
    template=code_prompt,
)
code_chain = LLMChain(llm=llm, prompt=code_prompt_template)
if __name__ == "__main__":
    # print(code_chain.run({'requirement' : "implementing the addition of a new employee functionality within the Spring framework",  
    #                       'abstract' : """
    # EmployeeController employeeService  jwtProperties  employeeLoginDTO  employee  claims  token  employeeLoginVO  employeeDTO  employeePageQueryDTO  pageResult  status  id  id  employee  employeeDTO  Result<EmployeeLoginVO> login(@RequestBodyEmployeeLoginDTOemployeeLoginDTO)  Result<String> logout()  Result save(@RequestBodyEmployeeDTOemployeeDTO)  Result<PageResult> page(EmployeePageQueryDTOemployeePageQueryDTO)  Result startOrStop(@PathVariableIntegerstatus,Longid)  Result getById(@PathVariableLongid)  Result update(@RequestBodyEmployeeDTOemployeeDTO)

    # Employee serialVersionUID  id  username  name  password  phone  sex  idNumber  status  createTime  updateTime  createUser  updateUser  
    
    # EmployeeDTO id  username  name  phone  sex  idNumber  
    
    # EmployeeService employeeLoginDTO  employeePageQueryDTO  status  id  id  employeeDTO  Employee login(EmployeeLoginDTOemployeeLoginDTO)  PageResult pageQuery(EmployeePageQueryDTOemployeePageQueryDTO)  void startOrStop(Integerstatus,Longid)  Employee getById(Longid)  void update(EmployeeDTOemployeeDTO)

    # EmployeeServiceImpl employeeMapper  employeeLoginDTO  username  password  employee  employeePageQueryDTO  page  total  records  status  id  employee  id  employee  employeeDTO  employee  Employee login(EmployeeLoginDTOemployeeLoginDTO)  PageResult pageQuery(EmployeePageQueryDTOemployeePageQueryDTO)  void startOrStop(Integerstatus,Longid)  Employee getById(Longid)  void update(EmployeeDTOemployeeDTO)
    # """}))

    print(code_chain.run({'requirement' : "implementing the addition of a new employee functionality within the Spring framework",  
                          'abstract' : """
        Exists_file: EmployeeController

        Attribute: employeeService  jwtProperties  employeeLoginDTO  employee  claims  token  employeeLoginVO  employeeDTO  employeePageQueryDTO  pageResult  status  id  id  employee  employeeDTO

        Method: Result<EmployeeLoginVO> login(@RequestBodyEmployeeLoginDTOemployeeLoginDTO)  Result<String> logout()  Result save(@RequestBodyEmployeeDTOemployeeDTO)  Result<PageResult> page(EmployeePageQueryDTOemployeePageQueryDTO)  Result startOrStop(@PathVariableIntegerstatus,Longid)  Result getById(@PathVariableLongid)  Result update(@RequestBodyEmployeeDTOemployeeDTO)

        Exists_file: Employee

        Attribute: serialVersionUID  id  username  name  password  phone  sex  idNumber  status  createTime  updateTime  createUser  updateUser   

        Exists_file: EmployeeDTO

        Attribute: id  username  name  phone  sex  idNumber

        Exists_file: EmployeeService

        Attribute: employeeLoginDTO  employeePageQueryDTO  status  id  id  employeeDTO

        Method: Employee login(EmployeeLoginDTOemployeeLoginDTO)  PageResult pageQuery(EmployeePageQueryDTOemployeePageQueryDTO)  void startOrStop(Integerstatus,Longid)  Employee getById(Longid)  void update(EmployeeDTOemployeeDTO)

        Exists_file: EmployeeServiceImpl

        Attribute: employeeMapper  employeeLoginDTO  username  password  employee  employeePageQueryDTO  page  total  records  status  id  employee  id  employee  employeeDTO  employee

        Method: Employee login(EmployeeLoginDTOemployeeLoginDTO)  PageResult pageQuery(EmployeePageQueryDTOemployeePageQueryDTO)  void startOrStop
        """}))

 