#  multiplication of two matrix 


def mat_multiplier(a, b):
    c = [ [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]
]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
               c[i][j] += a[i][k] * b[k][j]
    return c

a = [ [1, 2, 3],
      [2, 4, 5],
      [5, 6, 7]
]
b = [ [3, 2, 5], 
      [5, 6, 7],
      [8, 7, 9]
]
d = mat_multiplier(a, b)
for m in d:
    print(*m, sep = "\t")
                  
