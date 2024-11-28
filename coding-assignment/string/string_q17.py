# The Bus Number Confusion
# Story: You are tracking buses in a busy city, and each bus has a unique number. However, some of the bus numbers have been entered with spaces between the digits. You need to remove the spaces so that you can process the bus numbers correctly.

# Problem: Write a Python program that takes a string of bus numbers with spaces and removes the spaces between the digits
bus_number = input().split()
real_number = "".join(bus_number)
print(real_number)