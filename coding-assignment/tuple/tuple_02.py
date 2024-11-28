''' Write a Python program to count the elements in a list until an element is a 
tuple. '''
user = input().split()
count  = 0
for i in user:
    b = eval(i)
    if type(b) == tuple:
        break
    else:
        count +=1    
print(count)