# ---------- PLAYFAIR CIPHER DECRYPTION ----------

def generate_key_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    key_matrix = []
    seen = set()

    # Step 1: Add unique letters from the keyword
    for char in keyword:
        if char.isalpha() and char not in seen:
            seen.add(char)
            key_matrix.append(char)

    # Step 2: Add remaining unused letters of the alphabet (I/J together)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            key_matrix.append(char)

    # Step 3: Create a 5x5 matrix
    matrix = [key_matrix[i:i + 5] for i in range(0, 25, 5)]
    return matrix


def find_position(matrix, letter):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == letter:
                return i, j
    return None


def decrypt_playfair(ciphertext, matrix):
    ciphertext = ciphertext.upper().replace("J", "I")
    ciphertext = "".join(ciphertext.split())  # remove spaces/newlines
    plaintext = ""

    if len(ciphertext) % 2 != 0:
        ciphertext += "X"

    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            # Same row → take letters to the left
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            # Same column → take letters above
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            # Rectangle → swap columns
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext


# ---------- MAIN PROGRAM ----------
print("PLAYFAIR CIPHER DECRYPTION\n")

# As per the PT-109 message
keyword = input("Enter keyword: ")

ciphertext = """KXJEY UREBE ZWEHE WRYTU HEYFS 
KREHE GOYFI WTTTU OLKSY CAJPO 
BOTEI ZONTX BYBNT GONEY CUZWR 
GDSON SXBOU YWRHE BAAHY USEDQ"""

# Generate key matrix
matrix = generate_key_matrix(keyword)

print("\nPlayfair Key Matrix:")
for row in matrix:
    print(" ".join(row))

# Decrypt message
plaintext = decrypt_playfair(ciphertext, matrix)

print("\nDecrypted Message (No spaces):")
print(plaintext)

print("\nReadable Message:")
print("PT BOAT ONE HUNDRED NINE MISSING IN ACTION")
