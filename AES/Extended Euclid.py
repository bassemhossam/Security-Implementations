def extended_euclid(n, m):
    a1 = 1
    a2 = 0
    a3 = m
    b1 = 0
    b2 = 1
    b3 = n % m

    while 1:
        if b3 == 0:
            return "IMPOSSIBLE"
        if b3 == 1:
            return b2 % m
        q = a3//b3
        t1 = a1 - q * b1
        t2 = a2 - q * b2
        t3 = a3 - q * b3
        a1 = b1
        a2 = b2
        a3 = b3
        b1 = t1
        b2 = t2
        b3 = t3


line = input().split()
M = int(line[0])
N = int(line[1])
add_inverse = M - N % M
mul_inverse = extended_euclid(N, M)

if isinstance(mul_inverse,int):
    print(add_inverse, mul_inverse, sep=" ")
else:
    print("IMPOSSIBLE")
