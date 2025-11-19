def caesar_cipher(text, k):
    result = ""
    for char in text:
        if char.isalpha():  # Check if it's a letter
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + k) % 26 + shift)
        else:
            result += char  # Non-alphabet characters remain unchanged
    return result

# Main Program
text = input("Enter the text: ")
k = int(input("Enter shift value (1-25): "))

if 1 <= k <= 25:
    encrypted = caesar_cipher(text, k)
    decrypted = caesar_cipher(encrypted, 26 - k)

    print("\nOriginal Text : ", text)
    print("Encrypted Text: ", encrypted)
    print("Decrypted Text: ", decrypted)
else:
    print("Please enter a valid shift value between 1 and 25.")
