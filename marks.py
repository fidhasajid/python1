# Input marks | check pass / fail | store in dictionary

def pass_fail(maths,social,science,malayalam,english):
    final_result = 'pass'
    marklist = [maths,social,science,malayalam,english]
    for i in marklist:
        if i < 33:
            final_result = "fail"
    return final_result        


saeed     = pass_fail(1,2,3,4,5)
sameera   = pass_fail(10,11,12,13,14)
siham     = pass_fail(9,12,1,20,21)
hisham    = pass_fail(5,4,3,2,1)
safa      = pass_fail(5,6,7,8,9)
fidha     = pass_fail(60,46,47,48,49)

students_mark = [saeed,sameera,siham,hisham,safa,fidha]
students_mark_dict = {
     "saeed"   : saeed,
     "sameera" :sameera,
     "siham"   : siham,
     "hisham"  : hisham,
     "safa"    : safa,
     "fidha"   : fidha
 }
 
print(students_mark_dict)
