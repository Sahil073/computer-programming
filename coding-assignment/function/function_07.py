# sum of n natural numbers 
def sumer(n):
    count = 0
    for i in range(n+1):
        count += i
    return count
print(sumer(7))    #28
print(sumer(-5))    #0