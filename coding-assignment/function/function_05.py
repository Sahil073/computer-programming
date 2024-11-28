''' anagrram checker'''
def ana_checker(a, b):
    a1 = list(a)
    b1 = list(b)
    if len(a1) != len(b1):
        return False
    if a1.sort() == b1.sort():
        return True
    else:
        return False
print(ana_checker("Silent", "Listen"))    