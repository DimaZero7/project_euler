# https://projecteuler.net/problem=10
# python 3.10

import time


start_time = time.time()

limit = 2_000_000
last_prime_number = 7
prime_numbers = [2, 3, 5, last_prime_number]
# maximum divisor of prime numbers at the moment
maximum_divisor = 0

while limit > last_prime_number:
    # Step +2 to skip all multiples of 2
    last_prime_number += 2

    # We assume that the divisor of the next semisimple number will be in
    #   the range from maximum_divisor to maximum_divisor + N
    approximate_limit_maximum_divisor = maximum_divisor + 200

    for prime_number in prime_numbers:
        if prime_number >= approximate_limit_maximum_divisor:
            prime_numbers.append(last_prime_number)
            break
        if last_prime_number % prime_number == 0:
            maximum_divisor = max(maximum_divisor, prime_number)
            break
    else:
        prime_numbers.append(last_prime_number)

print(sum(prime_numbers))

end_time = time.time()
execution_time = end_time - start_time
print("Execution time: {:.6f} seconds".format(execution_time))
