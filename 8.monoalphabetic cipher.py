def generate_cipher_alphabet(keyword):
    keyword = keyword.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = ""

    # Step 1: Add unique letters from keyword
    for char in keyword:
        if char not in cipher and char.isalpha():
            cipher += char

    # Step 2: Add remaining unused letters
    for char in alphabet:
        if char not in cipher:
            cipher += char

    return cipher


def monoalphabetic_encrypt(plaintext, cipher_alphabet):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = plaintext.upper()
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            index = alphabet.index(char)
            ciphertext += cipher_alphabet[index]
        else:
            ciphertext += char  # Non-alphabet characters unchanged

    return ciphertext


def monoalphabetic_decrypt(ciphertext, cipher_alphabet):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            index = cipher_alphabet.index(char)
            plaintext += alphabet[index]
        else:
            plaintext += char

    return plaintext


# Example use
keyword = "CIPHER"
cipher_alphabet = generate_cipher_alphabet(keyword)
print("Generated Cipher Alphabet:", cipher_alphabet)

text = input("Enter plaintext: ")
ciphertext = monoalphabetic_encrypt(text, cipher_alphabet)
print("Encrypted Text:", ciphertext)

decrypted = monoalphabetic_decrypt(ciphertext, cipher_alphabet)
print("Decrypted Text:", decrypted)
