# taking input from user of matrix and doing subtraction
def subtract(m1, m2):
    c = []
    for i in range(len(m1)):
        l = []
        for j in range(len(m1[0])):
            l.append(0)
        c.append(l)  
    for i_ in range(len(m1)):
        for j_ in range(len(m1[0])):
            c[i_][j_] += m1[i_][j_] - m2[i_][j_]
    return c        


rm1, cm1 = list(map(int, input().split()))
m1 = []
for i in range(rm1):
    r1 = list(map(int, input().split()))
    m1.append(r1)
rm2, cm2 = list(map(int, input().split()))
m2 = []
for i in range(rm2):
    r2 = list(map(int, input().split()))
    m2.append(r2)       
d = subtract(m1, m2)
for mm in d:
    print(*mm, sep = "\t")