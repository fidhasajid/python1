
def pass_fail(maths,science):
    result = maths + science
    if result > 80:
        print("pass ok understand?")
    else:
        print("fail ok ?")
    return result

fidha = pass_fail(30,15)
saeed = pass_fail(90,90)

student_marks = [ fidha, saeed ]
student_marks_dict = {
    "fidha": fidha,
    "saeed": saeed,
}

print(student_marks_dict)