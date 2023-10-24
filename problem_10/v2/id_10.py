# https://projecteuler.net/problem=10
# python 3.11

import math

from utils import performance_decorator


@performance_decorator
def main():
    limit = 2_000_000
    last_number = 7
    prime_numbers = [2, 3, 5, last_number]

    while limit > last_number:
        last_number += 2
        last_number_sqrt = math.sqrt(last_number)

        for prime_number in prime_numbers:
            if last_number % prime_number == 0:
                break

            if prime_number >= last_number_sqrt:
                prime_numbers.append(last_number)
                break

    print(sum(prime_numbers))


main()
