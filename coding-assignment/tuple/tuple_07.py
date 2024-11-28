# 1 Merge two tuples, alternating elements from each
l1 = eval(input())
l2 = eval(input())
new_list = []
for i in range(len(l1)):
    new_list.append(l1[i])
    new_list.append(l2[i])
print(new_list)          

