# write a programme two find the prime numbr between two given numbers.
def prime_ranfinder(a, b):
    prime_numbers = []
    for i in range(a, b):
        count = 0
        for j in range(2, i**1/2):
            if i % j == 0:
                count += 1
        if count == 0:
            prime_numbers.append(i)
        else:
            continue 
    return prime_numbers           
print(prime_ranfinder(1, 10))