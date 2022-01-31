fidha = "fidha"
fidha_list = ['f', 1, 'd', 'h', 'a']

print(fidha[1])
print(fidha[1:])
print(fidha[:3])
print(fidha[1:3])
print(fidha[-1])

print(fidha_list[1])
print(fidha_list[1:])
print(fidha_list[:3])
print(fidha_list[1:3])


fidha_list.pop()
print(fidha_list)
fidha_list.insert(len(fidha_list), 'a')
print(fidha_list)

fidha_list.remove('h')
print(fidha_list)
fidha_list.insert(3, 'h')
print(fidha_list)
