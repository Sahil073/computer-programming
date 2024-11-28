# find wheather the number is prime or not
def prime_checker(a):
    count = 0 
    for i in range(2, a):
        if a % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False  
print(prime_checker(5))
print(prime_checker(4))
print(prime_checker(6))
print(prime_checker(33))
print(prime_checker(100))
