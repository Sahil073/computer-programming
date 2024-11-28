'''The Shopping List Helper'''
lst1 = input().split()
lst2 = input().split()
for i in lst2:
    if i not in lst1:
        lst1.append(i)
        
print(*lst1)