n = int(input())
def leap_year_checker(n):
    for i in range(n+1):
        if i % 4 == 0 and i % 100 != 0:
            print(i) 
print(leap_year_checker(n))            