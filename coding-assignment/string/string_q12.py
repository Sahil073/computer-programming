'''The Secret Code'''
user_input = input()
code = ''
for i in user_input:
    if i == "z" or i == "Z":
        s = 65
    else:
        s = ord(i) + 1
    code += chr(s)
print(code)    