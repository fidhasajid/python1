class Company:
    comp_name = ''

    def __init__(self, name):
        self.comp_name = name

class Department(Company):

    dep_name = ''

    def __init__(self, dep_name, company_name):
        self.fidha(dep_name, company_name)
    
    def fidha(self, dep_name, company_name):
        super().__init__(company_name)
        self.dep_name = dep_name

class Company2:
    comp2_name = ''
    gst = ''
    address = ''

    def __init__(self, name):
        self.comp2_name = name
    
    def fidha2(self, name):
        self.comp2_name = name

class Employee(Department, Company2):
    emp_name = ''

    def __init__(self, emp_name, dep_name, comp_name):
        super().__init__(dep_name, comp_name)
        super().fidha2(comp_name)
        self.name = emp_name

new_emp = 'saeed'
saeed = Employee(new_emp, 'IT', 'vesela')
print(saeed.dep_name)
print(saeed.comp_name)

