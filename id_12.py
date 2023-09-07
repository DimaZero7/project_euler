# https://projecteuler.net/problem=12
# python 3.10

# The decision is based on this article
# https://zaochnik-com.com/spravochnik/matematika/delimost/nahozhdenie-vseh-delitelej-chisla/


def get_prime_divisor(number: int) -> int:
    if number % 2 == 0:
        return 2

    divisor = 3
    while divisor <= number:
        if number % divisor == 0:
            return divisor

        divisor += 2


def count_elements(elements: list) -> dict:
    counts = {}

    for element in elements:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1

    return counts


stop = False

last_number = 1
sequence_sum = 1

while not stop:
    last_number += 1
    sequence_sum += last_number

    decomposition_complete = False

    divisible = sequence_sum
    prime_divisors = []

    while not decomposition_complete:
        prime_divisor = get_prime_divisor(divisible)

        prime_divisors.append(prime_divisor)
        divisible /= prime_divisor

        if divisible == 1:
            decomposition_complete = True

    divisor_count = 1
    for i in count_elements(elements=prime_divisors).values():
        divisor_count *= i + 1

    if divisor_count > 500:
        stop = True

print(sequence_sum)
