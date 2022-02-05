"""
Create class: Student -> inherit Family
    Variables:
        name: string
        class_number: integer
        division: string
        gender: string
        marks: dictionary
            - science, maths
        attendance: list / array (10 days)
            True / False
    
    Functions:
        change_marks | Science / Math
        update_attendance - insert (True / False)
        check_pass:
            check passed in math / science | Score > 40 | -> print
    
Create class Class_Division:
    Variable:
        student_list: list
        class_teacher: string

    Function:
        add_student
            student_list -> add
        change_teacher
        list_all_students:
            print all students

Create class Family
    Variable: 
        father_name: string
        mother_name: string
        siblings: list
"""


class Class_division:
    student_list = []
    class_teacher = 'teacher'

    def add_student(self, name):
        len_stud = len(self.student_list)
        self.student_list.insert(len_stud, name)
    
    def assign_class_teacher(self, name):
        self.class_teacher = name
    
    def list_all_students(self):
        for i in self.student_list:
            print(i)

class Family:
    father_name = ''
    mother_name = ''
    sibling = []

class Student(Family):
    name = ''
    class_number = 0
    division = ''
    gender = ''
    marks = {}
    sub_list = []
    attendance = []

    def add_subject(self, subject):
        self.sub_list.insert(len(self.sub_list), subject)
        self.marks[subject] = 0

    def update_attendance(self, attended):
        len_atten = len(self.attendance)
        self.attendance.insert(len_atten, attended)

    def change_marks(self, subject, mark):
        self.marks[subject] = mark

    def check_pass(self, subject):
        if self.marks[subject] > 40:
            print("pass")
        else:
            print("fail")


safa = Student()

print(safa.sub_list)

safa.add_subject("maths")
safa.add_subject("science")
print(safa.sub_list)

print(safa.marks)