# https://projecteuler.net/problem=1

def sum_multiples(number: int, to: int):
    sum_numbers = 0
    term = 0

    while term + number < to:
        term += number
        sum_numbers += term

    return sum_numbers


end = 1000

number_one = 3
number_two = 5

print(
    sum_multiples(number_one, end) + sum_multiples(number_two, end) -
    sum_multiples(number_one * number_two, end)
)
