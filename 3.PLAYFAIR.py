# Simple Playfair Cipher Program

def generate_key(key):
    key = key.replace("j", "i").lower()
    result = ""
    for c in key:
        if c not in result and c.isalpha():
            result += c
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c not in result and c != "j":
            result += c
    return [list(result[i:i+5]) for i in range(0, 25, 5)]

def find_pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

def encrypt_pair(a, b, matrix):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)
    if r1 == r2:
        return matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
    elif c1 == c2:
        return matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def playfair_encrypt(text, key):
    matrix = generate_key(key)
    text = text.replace("j", "i").replace(" ", "").lower()
    if len(text) % 2 != 0:
        text += 'x'
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'x'
        if a == b:
            b = 'x'
        result += encrypt_pair(a, b, matrix)
        i += 2
    return result

# Main
key = input("Enter key: ")
text = input("Enter plaintext: ")

encrypted = playfair_encrypt(text, key)
print("Encrypted text:", encrypted)
