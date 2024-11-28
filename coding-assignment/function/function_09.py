# Write a Python function that takes a list of numbers and returns a new list with all the even numbers.
def even_lover(arr):
    evens = []
    for i in arr:
        if int(i) % 2 == 0:
            evens.append(i)
    return evens
print(*even_lover(input("Enter your arr:").split()))

        