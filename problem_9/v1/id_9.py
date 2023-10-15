# https://projecteuler.net/problem=9
# python 3.10

for a in range(1, 1000 + 1):
    for b in range(a + 1, 1000 + 1):
        c = 1000 - a - b
        if a**2 + b**2 == c**2 and a + b + c == 1000:
            print(a * b * c)
