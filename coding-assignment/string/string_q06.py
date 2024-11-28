'''The Library Book Tracker'''
user_input = input().split(",")
sorted_names = sorted(user_input)
for i in sorted_names:
    print(i)