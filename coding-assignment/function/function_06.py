# palindrom checker
def palindrom_checker(a, b):
    if a[::-1] == b:
        return True
    return False
print(palindrom_checker("sahil", "lihas"))