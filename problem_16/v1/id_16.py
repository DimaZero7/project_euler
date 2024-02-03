# https://projecteuler.net/problem=16
# python 3.11
from utils import performance_decorator


@performance_decorator
def main():
    number = 2 ** 1000
    digits_list = [int(digit) for digit in str(number)]
    print(sum(digits_list))


main()
