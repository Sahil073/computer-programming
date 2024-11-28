# majority element display kar dunga...
def major_narr(a):
    majority = []
    for i in a:
        if a.count(i) > len(a)//2:
            if i not in majority:
                majority.append(i)
    return majority 
print(*major_narr(input("Enter your arr:").split()))
       