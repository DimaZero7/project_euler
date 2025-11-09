# https://projecteuler.net/problem=20
# python 3.11
import math

from utils import performance_decorator

@performance_decorator
def main():
    factorial_number = 100
    factorial_product = math.factorial(factorial_number)
    factorial_number_ist = [int(i) for i in str(factorial_product)]
    sum_number = sum(factorial_number_ist)
    print(sum_number)


main()
