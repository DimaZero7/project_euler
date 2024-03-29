# https://projecteuler.net/problem=6
# python 3.10
from utils import performance_decorator


@performance_decorator
def main():
    minuend = 0
    subtrahend = 0

    for i in range(1, 100 + 1):
        subtrahend += i * i
        minuend += i

    print(minuend * minuend - subtrahend)


main()
