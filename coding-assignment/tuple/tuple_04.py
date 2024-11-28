''' Write a Python program to replace last value of tuples in a list.    
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)] '''
user_input = eval(input())
new_list = []
for i in user_input:
    c = list(i)
    c[-1] = 100
    d = tuple(c)
    new_list.append(d)
print((new_list))    
