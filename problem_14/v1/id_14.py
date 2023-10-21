# https://projecteuler.net/problem=14
# python 3.11

import time


start_time = time.time()

end_number = 1_000_000
max_count = 0
max_number = 0


for number in range(1, end_number + 1):
    if number - 1 % 3 == 0:
        continue

    stop = False
    number_count = 1
    start_number = number

    while not stop:
        if number % 2 == 0:
            number /= 2
            number_count += 1
        else:
            number = number * 3 + 1
            number_count += 1

        if number == 1:
            stop = True
            if number_count > max_count:
                max_count = number_count
                max_number = start_number

print(max_count, max_number)

end_time = time.time()
execution_time = end_time - start_time
print("Execution time: {:.6f} seconds".format(execution_time))
