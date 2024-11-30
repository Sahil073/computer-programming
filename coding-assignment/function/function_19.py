rm1, cm1 = list(map(int, input().split()))
m1 = []
for i in range(rm1):
    r = list(map(int, input().split()))
    m1.append(r)
    
rm2, cm2 = list(map(int, input().split()))
m2 = []
for j in range(rm2):
    r = list(map(int, input().split()))
    m2.append(r)
c = []
for i_ in range(rm1):
    l = []
    for j_ in range(cm2):
        l.append(0)
    c.append(l)
for i__ in c:
    print(i__) 
for _ in range(rm1):
    for __ in range(cm2):
        for k_ in range(rm2):
            c[_][__] += m1[_][k_] * m2[k_][__]
for i in c:
    print(*i)                
