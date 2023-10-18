# https://projecteuler.net/problem=10
# python 3.11

import math
import time


start_time = time.time()

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


end_time = time.time()
execution_time = end_time - start_time
print("Execution time: {:.6f} seconds".format(execution_time))
