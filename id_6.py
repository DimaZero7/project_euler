# https://projecteuler.net/problem=6


minuend = 0
subtrahend = 0

for i in range(1, 100 + 1):
    subtrahend += i * i
    minuend += i


print(minuend * minuend - subtrahend)
