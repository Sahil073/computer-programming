'''
 Write the program where the user enters a string and a substring. You have to print the 
number of times that the substring occurs in the given string. String traversal will take place from 
left to right, not from right to left. 
'''
user_input = input()
sub_string = input()
count = 0
for i in range(len(user_input)-len(sub_string)+1):
    if user_input[i:i+len(sub_string)] == sub_string:
        count +=1
print(count)        


