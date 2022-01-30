class University:

    univ_name = 'Kerala'

class Institution(University):

    inst_name = 'Girls School'

    def ndksa(self):
        print('dsa')

class Student(Institution):

    name = ''
    class_num = 0
    division = ''
    gender = ''
    age = 0
    medium = ''
    dob = ''
    address = ''

    def __init__(self, name, class_num, division, gender, age, medium = 'english', dob = '', address = ''):
        self.name = name
        self.class_num = class_num
        self.division = division
        self.gender = gender
        self.age = age
    
    def student_update(self, class_num, division, age):
        self.class_num = class_num
        self.division = division
        self.age = age



class Fruit:
    color = ''
    smell = ''
    vitamin = ''
    shape = ''

    def __init__(self, color, smell, vitamin, shape):
        self.color = color
        self.smell = smell
        self.vitamin = vitamin
        self.shape = shape
    
    def change_color(self, color):
        self.color = color
    

orange = Fruit('orange', 'Sweet', 'C', 'Round')
orange.change_color('Red')
print(orange.color)
apple = Fruit('orange', 'Sweet', 'C', 'Round')