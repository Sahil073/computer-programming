'''The Shortest Word Finder'''
user_input = input().split()
shortest_word = user_input[0]
for i in user_input:
    if len(i) < len(shortest_word):
        shortest_word = i
print(shortest_word)
