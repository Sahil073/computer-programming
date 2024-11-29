# taking matrik as input from user and then multiply them
rm1, cm1 = list(map(int, input().split()))
m1 = []
for i in range(rm1):
    r1 = list(map(int , input().split()))
    m1.append(r1)
rm2, cm2 = list(map(int, input().split())) 
m2 = []   
for j in range(rm2):
    r2 = list(map(int , input().split()))
    m2.append(r2)
# now creating a function for mulitplying matrix.
def mati_multipler(m1, m2 , cm1, rm2):
    if cm1 != rm2:
        return False
    c = []
    for _ in range(cm1):
        l = []
        for __ in range(rm2):
            l.append(0) 
        c.append(l)
    for i_ in range(rm1):
        for j_ in range(cm2):
            for k_ in range(rm2):
                c[i_][j_] += m1[i_][k_] * m2[k_][j_]
    return c          
d = (mati_multipler(m1, m2, cm1, rm2))
for ir in d:
    print(*ir, sep = "\t")

