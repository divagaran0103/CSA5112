import string
import random

# Generate a random substitution key (cipher alphabet)
def generate_key():
    letters = list(string.ascii_uppercase)
    shuffled = letters.copy()
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))

# Encrypt the plaintext using the generated key
def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext.upper():
        if char in key:
            ciphertext += key[char]
        else:
            ciphertext += char  # Non-alphabet characters remain unchanged
    return ciphertext

# Decrypt the ciphertext using the same key
def decrypt(ciphertext, key):
    reversed_key = {v: k for k, v in key.items()}
    plaintext = ""
    for char in ciphertext.upper():
        if char in reversed_key:
            plaintext += reversed_key[char]
        else:
            plaintext += char
    return plaintext

# Main Program
if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    
    key = generate_key()
    print("\nGenerated Substitution Key:")
    for p, c in key.items():
        print(f"{p} -> {c}")
    
    ciphertext = encrypt(plaintext, key)
    print("\nEncrypted Text:", ciphertext)
    
    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)
