# https://projecteuler.net/problem=3


def get_divisor(number: int):
    for i in range(2, number + 1):
        if number % i == 0:
            return i


number = 600851475143
max_divisor = 0

while number != 1:
    divisor = get_divisor(number=number)
    max_divisor = max(divisor, max_divisor)
    number = int(number / divisor)

print(max_divisor)
