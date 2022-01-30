# Class -- Employee, Department, Company
# Department - Performance - variable
# Company - address - variable
# Change Department

class Company:
    company_name ='fidhas company'
    company_adress = 'jubilee road'

class Department(Company):
    department_name ='it department'

class Employee(Department):

    name = ''
    age = 0
    gender = ''
    department = ''
    adress = ''

    def __init__(self, name_, age, gender, department, adress):
        self.name = name_
        self.age = age
        self.gender = gender
        self.department = department
        self.adress = adress

    def change_department(self, department):
        self.department =department



fidha = Employee('fidha','24','female','it','jubilee road')
print(fidha.company_name)
print(fidha.department_name)
print(fidha.name)
print(fidha.age)
print(fidha.gender)
print(fidha.department)
print(fidha.adress)

fidha.change_department('financial')

print(fidha.department)
