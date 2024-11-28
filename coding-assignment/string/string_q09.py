'''The Sentence Fixer'''
user_input = input().split('.')
l = []
if user_input[-1] == ".":
    user_input.pop()
for i in user_input:
    d = i.strip()
    c = d.capitalize()
    l.append(c+".")
print(*l)    
# 2nd approch
def capitalize(para):
    liti_para = para.split(". ")
    capitalize_para = [i.capitalize() for i in liti_para]
    final_para = ". ".join(capitalize_para)
    return final_para
print(capitalize(input("enter your text:")))
