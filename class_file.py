from class_intro import *

fidha = Student('fidha', 9, 'B', 'Female', 15)
print(fidha.univ_name)
print(fidha.inst_name)
print(fidha.name)
print(fidha.age)
print(fidha.class_num)
print(fidha.division)

print('*******************************')

fidha.student_update(10, 'C', 16)
print(fidha.age)
print(fidha.class_num)
print(fidha.division)

print('*******************************')

saeed = Student('saeed', 99, 'B', 'Male', 28)
print(saeed.name)
print(saeed.age)

saeed.student_update(10, 'C', 16)
