def is_power_of_two(n): 
    if n <= 0: 
        return False 
    while n % 2 == 0: 
        n /= 2 
    return n == 1
print(is_power_of_two(12))
