# Story: You have received an encrypted message where each character has been shifted forward by a fixed number in the alphabet. For example, if the shift is 2, 'a' becomes 'c', 'b' becomes 'd', and so on. You need to decrypt the message by shifting the characters back to their original positions.

# Problem: Write a Python program that takes an encrypted message and a shift value, then prints the decrypted message.
encrypted_code = input("message:")
decrypt_code = ''
for i in encrypted_code:
    c = ord(i) - 2
    decrypt_code += chr(c)
print(decrypt_code)    