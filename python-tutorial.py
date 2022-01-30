
a = input("Please Enter mark: ")

def pass_fail(a):
    if (a > 100):
        print("Incorrect value. Maryatikulla value enter cheyyuka!")
    elif (a > 40):
        print("pass")
    else:
        print("fail")

pass_fail(int(a))