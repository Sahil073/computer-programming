'''Repeated Names in the Village
Story: In a small village, there are many people with the same names. You have a list of names of people in the village, and your task is to remove the duplicates and print only the unique names.

Problem: Write a Python program that takes a list of names and removes any duplicates, then prints the unique names.'''
user_input = input().split()
unique_list = []
for i in user_input:
    if i not in unique_list:
        unique_list.append(i)
print(*unique_list)        