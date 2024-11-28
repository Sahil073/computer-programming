#  Find all unique elements in a tuple, preserving order
user_input = eval(input())
list_tuple = list(user_input)
new_tuple = []
for i in user_input:
    if i not in new_tuple:
        new_tuple.append(i)
print(tuple(new_tuple))        