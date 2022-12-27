# https://projecteuler.net/problem=2

numbers = [1, 2]

sum_even_values = 2  # 2 is an even fibonacci number which is already known


while numbers[1] < 4_000_000:
    sum_numbers = numbers[0] + numbers[1]

    if sum_numbers % 2 == 0:
        sum_even_values += sum_numbers

    numbers.append(sum_numbers)
    del numbers[0]

print(sum_even_values)
