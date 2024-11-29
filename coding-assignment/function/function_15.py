# sun of diagonal of the matrix
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

def diagonal_sum(a):
    sum_ = 0
    for i in range(len(a)):
        sum_ += a[i][i]
    return sum_        
print(diagonal_sum(a))
