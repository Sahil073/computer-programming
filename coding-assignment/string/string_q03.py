'''The Duplicate Word Finder'''
user_input = input().split()
duplicate_words = []
for i in user_input:
    if user_input.count(i) > 1 and i not in duplicate_words:
        duplicate_words.append(i)
print(*duplicate_words)       