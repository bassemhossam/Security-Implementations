line = input().split()
F = line[0]
G = line[1]
F_int = int(F, 16)
G_int = int(G, 16)
F_bin = bin(F_int)[2:].zfill(8)
G_bin = bin(G_int)[2:].zfill(8)

# addition
add = F_int ^ G_int
add_hex = hex(add)[2:].upper()
if len(add_hex) == 1:
    add_hex = "0"+add_hex


# multiplication

if G_int > 0 and F_int > 0:

    F_result = [F_int]

    for i in range(1, 8):
        if F_result[i-1] >= 128:
            F_result.append(((F_result[i-1] << 1)-256) ^ 27)
        else:
            F_result.append(F_result[i-1] << 1)
    indices = [z for z, x in enumerate(reversed(G_bin)) if x == "1"]

    mul = 0
    for i in indices:
        mul = mul ^ F_result[i]

    mul_hex = hex(mul)[2:].upper()
    if len(mul_hex) == 1:
        mul_hex = "0" + mul_hex
else:
    mul_hex = "00"

print(add_hex, mul_hex, sep=" ")

