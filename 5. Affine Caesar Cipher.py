import math  # ✅ Correct import

# Encryption function
def encrypt(text, a, b):
    result = ""
    for char in text.lower():
        if char.isalpha():
            p = ord(char) - ord('a')
            c = (a * p + b) % 26
            result += chr(c + ord('a'))
        else:
            result += char
    return result

# Modular inverse function
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Decryption function
def decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Error: 'a' has no modular inverse. Invalid key!"
    for char in cipher.lower():
        if char.isalpha():
            c = ord(char) - ord('a')
            p = (a_inv * (c - b)) % 26
            result += chr(p + ord('a'))
        else:
            result += char
    return result

# Main Program
text = input("Enter plaintext: ")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# Check if 'a' is valid (coprime with 26)
if math.gcd(a, 26) != 1:
    print("Invalid 'a'! gcd(a,26) must be 1. Not one-to-one mapping.")
else:
    encrypted = encrypt(text, a, b)
    decrypted = decrypt(encrypted, a, b)

    print("\nEncrypted text:", encrypted)
    print("Decrypted text:", decrypted)
