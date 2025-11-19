import math

# Total letters in Playfair (I/J combined)
n = 25

# Calculate log2(25!) to express number of keys as power of 2
log2_factorial = sum(math.log2(i) for i in range(1, n + 1))

print(f"Approximate total number of Playfair keys (25!) = 2^{log2_factorial:.2f}")

# Considering duplicates: effectively unique keys
# From cryptanalysis, roughly 2^78
print("Approximate number of effectively unique Playfair keys ≈ 2^78")
