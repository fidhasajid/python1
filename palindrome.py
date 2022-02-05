word = 'malayaffjram'
j = -1
for i in word:
    j_in_word = word[j]
    if i == j_in_word:
        mark = "right"   
    else:
        mark = "wrong"
        break
    j = j-1

if mark == "right":
    print("good")
else:
    print("bad")
