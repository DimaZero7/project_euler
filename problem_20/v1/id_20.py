# https://projecteuler.net/problem=20
# python 3.11
from utils import performance_decorator

@performance_decorator
def main():
    factorial_number = 100
    factorial_product = 1
    sum_number = 0

    for i in range(1, factorial_number + 1):
        factorial_product *= i

    factorial_number_str = str(factorial_product)

    for i in factorial_number_str:
        sum_number += int(i)

    print(sum_number)


main()
