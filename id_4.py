# https://projecteuler.net/problem=4


largest_three_digit_number = 999
max_product = 0

for first_multiplier in range(1, largest_three_digit_number + 1):
    for last_multiplier in range(1, largest_three_digit_number + 1):
        product = first_multiplier * last_multiplier
        if str(product) == str(product)[::-1]:
            if max_product < product:
                max_product = product

print(max_product)
