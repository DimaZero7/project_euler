# https://projecteuler.net/problem=5

number_not_found = True
number = 20

# exclude 1 because all numbers divisible by 1
# exclude all numbers that are divisible by 20 without a remainder, because step 20 means that the resulting number will always be divisible by 2, 4, 5, 10
# excluded are numbers that, when multiplied by 2, give a number from the list, for example 6 * 2 = 12 These numbers are: 6, 7, 8, 9
dividers = [3, 11, 12, 13, 14, 15, 16, 17, 18, 19]

while number_not_found:
    for i in dividers:
        if number % i != 0:
            # step 20 for optimization - it makes no sense to count numbers in the range n + 20 because they will not be divisible by 20
            number += 20
            break
        if i == dividers[-1]:
            number_not_found = False

print(number)
