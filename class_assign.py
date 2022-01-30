# Class -- Employee, Department, Company
# Department - Performance - variable
# Company - address - variable
# Change Department

class Company:
    company_name ='fidhas company'

class Department(Company):
    department_name ='it department'



class Employee(Department):

    name = ''
    age = 0
    gender = ''
    department = ''
    adress = ''

    def __init__(self, name, age, gender, department, adress):
        self.name = name
        self.age = age
        self.gender = gender
        self.department = department
        self.adress = adress


fidha = Employee('fidha','24','female','it','jubilee road')
print(fidha.company_name)
print(fidha.department_name)
print(fidha.name)
print(fidha.age)
print(fidha.gender)
print(fidha.department)
print(fidha.adress)

