marks_final = {}
person_final = {}
sub_list = ["maths","social","science","malayalam","english"]
pers_list = ["saeed", "sameera", "siham", "hisham", "fidha", "safa"]

def create_mark_dict(mark, result):
    return {
        "mark": mark,
        "result": result
    }

for i in sub_list:
    marks_final[i] = create_mark_dict(45, "pass")

for i in pers_list:
    person_final[i] = marks_final

print(person_final)
