def addition(a ,b):
    added_matrix = []
    for i in range(len(a)):
        l = []
        for j in range(len(a[0])):
            l.append(0)
        added_matrix.append(l)    
    for i_ in range(len(a)):
        for j_ in range(len(a[0])):
            added_matrix[i_][j_] = a[i_][j_] + b[i_][j_]  
    return added_matrix                                   
           
# pre defined matrix addition
a = [ [5, 6, 7],
    [2, 3, 4],
    [8, 9, 5]
]
b = [ [6, 5, 0],
    [2, 3, 3],
    [3, 6, 8]
]
d = addition(a, b)
for ii in d:
    for ij in ii:
        print(str(ij).zfill(2), end = ' ', sep = '')
    print()    
