from math import sqrt, floor


def calculate(n: int):
    upper_bound = floor(sqrt(n))

    numbers_gen = (x for x in range(upper_bound + 1))

    numbers_filtered = filter(lambda x: x % 2 == 0, numbers_gen)

    numbers_pow2 = map(lambda x: x * x, numbers_filtered)

    print(list(numbers_pow2))


calculate(int(input("pana la cat sa cautam pp: ")))
