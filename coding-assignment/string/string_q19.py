'''The Password Validator
Story: In a cybersecurity class, you are learning about strong passwords. Your teacher has given you a list of passwords and asked you to determine which passwords are "strong". A strong password is defined as one that has at least 8 characters, contains both uppercase and lowercase letters, and has at least one number.

Problem: Write a Python program that reads a list of passwords and prints "strong" if the password is strong, otherwise "weak".
'''
import re

def is_strong_password(password):
    
    if len(password) < 8:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    return True

def check_passwords(password_list):
    strong_passwords = []
    for password in password_list:
        if is_strong_password(password):
            strong_passwords.append(password)
    return strong_passwords

# Example usage
passwords = [
    "Password123",
    "weakpass",
    "StrongPass1",
    "12345678",
    "Passw0rd!",
    "short1A",
    "ValidPass123"
]

strong_passwords = check_passwords(passwords)
print("Strong passwords are:", strong_passwords)

