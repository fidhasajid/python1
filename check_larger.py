# Check the largest number

#1Q

num1 = 54
num2 = 21
num3 = 43

if (num1 > num2):
    if(num1 > num3):
        print("num 1 is " + str(num1))
    else:
        print("num3 is greater" + str(num3))
else:
    if(num2 > num3):
        print("num2 is greater" + str(num2))
    else:
        print("num3 is greater" + str(num3))

#2Q
numbers = [43, 53578439247, 10, 84, 321, 12, 7942, 43, 984032]

largest_number = -999

for i in numbers:
    for j in numbers:
        if i >= j and i >= largest_number:
            largest_number = i
        elif j > largest_number:
            largest_number = j

print(largest_number)

numbers.sort()
new_number = numbers[-1]

print("new_largest number " + str(new_number))

