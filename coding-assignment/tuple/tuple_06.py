'''Tuple Methods and Operations
Given the tuple:

python
t = (5, 10, 15, 10, 20, 10, 25, 10)
Find the index of the first occurrence of 10.

Count how many times 10 appears in the tuple.

Create a new tuple by replacing every occurrence of 10 with 100.
'''
user = eval(input())
luser = list(user)
for i in range(len(luser)):
    if luser[i] == 10:
        print(i)
        break
        
print(f'10 occurs {luser.count(10)}')
for i in range(len(luser)):
    if luser[i] == 10:
        luser[i] = 100    
      
new_tuple = tuple(luser)
print(new_tuple)      