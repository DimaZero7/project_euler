# https://projecteuler.net/problem=9
# python 3.10


for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = 1000 - a - b
        if c > 0 and a**2 + b**2 == c**2:
            print(a * b * c)
            break
