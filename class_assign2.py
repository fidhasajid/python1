
class Employee():

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

    def create_employee(self, name_, age, gender, department, adress):
        self.name = name_
        self.age = age
        self.gender = gender
        self.department = department
        self.adress = adress

    def change_department(self, department):
        self.department =department






fidha = Employee('Fidha', 16, 'F', 'IT', 'J')


print(fidha.name)








