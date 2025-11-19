# Affine Cipher Decryption (Breaking Example)

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def decrypt(cipher, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Invalid key, no inverse for a."
    result = ""
    for char in cipher.upper():
        if char.isalpha():
            c = ord(char) - ord('A')
            p = (a_inv * (c - b)) % 26
            result += chr(p + ord('A'))
        else:
            result += char
    return result

# Given
ciphertext = input("Enter ciphertext: ")

# From frequency analysis
a = 3
b = 15

decrypted = decrypt(ciphertext, a, b)
print("\nAssumed key values: a =", a, ", b =", b)
print("Decrypted text:", decrypted)
