def digit_adder(n):
    m = str(n)
    sum_ = 0
    for i in m:
        sum_ += int(i)
    return sum_

n = int(input("Enter a number: "))
while n >= 10:
    n = (digit_adder(n))

print("Final result:", n)
