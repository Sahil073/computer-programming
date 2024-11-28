# Task: Write a function that takes a tuple of tuples (a 2D matrix-like structure) of integers and returns a tuple where each element is the sum of the corresponding columns of the input tuples.
rows = int(input())
column = int(input())
matrix = []
for i in range(rows):
    elements = input().split()
    matrix.append(elements)
sum_columns = []
for i in range(column):
    sum = 0
    for j in range(rows):
        sum += int(matrix[j][i])
    sum_columns.append(sum)
print(sum_columns)           