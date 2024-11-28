''' Write a Python program to remove an empty tuple(s) from a list of tuples.    
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')] 
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd'] '''
user_input = eval(input())
new_list = []
for i in user_input:
    if not len(i) != 0 and type(i) == tuple:
        user_input.remove(i)
print(user_input)        
