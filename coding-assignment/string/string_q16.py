'''The Repeated Word Finder
Story: You are reading a large book, and you want to find out which words are repeated the most. Your task is to write a Python program that takes a paragraph of text and prints the most frequent word(s).

Problem: Write a Python program that reads a paragraph and prints the word that appears the most frequently.
'''
user_input = (input()).split()
most_frequent = user_input[0]
count_most_frequent = user_input.count(user_input[0])
for i in range(len(user_input)):
    if user_input.count(user_input[i]) > count_most_frequent:
        most_frequent = user_input[i]
        count_most_frequent = user_input.count(user_input[i])
print(most_frequent)        


