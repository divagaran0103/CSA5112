# ---------- PLAYFAIR CIPHER ENCRYPTION (USING GIVEN MATRIX) ----------

def find_position(matrix, letter):
    """Return (row, col) of letter in matrix."""
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == letter:
                return i, j
    return None


def prepare_text(text):
    """
    Prepare the plaintext:
    - Uppercase, replace J -> I
    - Remove non-letters
    - Split into digraphs, inserting 'X' between identical letters in a pair
    - If final single letter remains, append 'X'
    """
    text = text.upper().replace("J", "I")
    letters = [ch for ch in text if ch.isalpha()]

    digraphs = []
    i = 0
    while i < len(letters):
        a = letters[i]
        # if there is a next letter
        if i + 1 < len(letters):
            b = letters[i + 1]
            if a == b:
                # identical pair -> insert X after a, advance by 1
                digraphs.append(a + "X")
                i += 1
            else:
                digraphs.append(a + b)
                i += 2
        else:
            # last single letter -> pad with X
            digraphs.append(a + "X")
            i += 1

    return digraphs


def encrypt_playfair(plaintext, matrix):
    digraphs = prepare_text(plaintext)
    ciphertext_pairs = []

    for pair in digraphs:
        a, b = pair[0], pair[1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 is None or r2 is None:
            raise ValueError(f"Letter not found in matrix: {a} or {b}")

        # Rule 1: same row -> take letter to the right (wrap)
        if r1 == r2:
            c_a = matrix[r1][(c1 + 1) % 5]
            c_b = matrix[r2][(c2 + 1) % 5]
        # Rule 2: same column -> take letter below (wrap)
        elif c1 == c2:
            c_a = matrix[(r1 + 1) % 5][c1]
            c_b = matrix[(r2 + 1) % 5][c2]
        # Rule 3: rectangle -> swap columns
        else:
            c_a = matrix[r1][c2]
            c_b = matrix[r2][c1]

        ciphertext_pairs.append(c_a + c_b)

    # return both joined ciphertext and grouped digraphs for readability
    ciphertext = "".join(ciphertext_pairs)
    grouped = " ".join(ciphertext_pairs)
    return ciphertext, grouped, digraphs


# ---------- MAIN (matrix from the question) ----------
matrix = [
    ['M', 'F', 'H', 'I', 'K'],
    ['U', 'N', 'O', 'P', 'Q'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['E', 'L', 'A', 'R', 'G'],
    ['D', 'S', 'T', 'B', 'C']
]

message = "Must see you over Cadogan West. Coming at once."

ciphertext, grouped, digraphs = encrypt_playfair(message, matrix)

print("Playfair Matrix:")
for row in matrix:
    print(" ".join(row))

print("\nPrepared digraphs (after cleaning & X-insertion):")
print(", ".join(digraphs))

print("\nEncrypted ciphertext (no spaces):")
print(ciphertext)

print("\nEncrypted ciphertext (grouped digraphs):")
print(grouped)
