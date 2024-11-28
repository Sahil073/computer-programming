''' Write a Python program to sort a tuple by its float element.    
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')] 
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')] '''
user = input().split(",")
new_list = []
for i in user:
    c = list(i)
    c.sort()
    c.reverse()
    d = tuple(i)
    new_list.append(d)
new_list.reverse()
print(new_list)    
    