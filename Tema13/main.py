from more_itertools import map_reduce, chunked
from functools import reduce


def ex2():
    words = "o yeah scula bob copilu strazii m am nascut la semafor direct o o yeah calutu jonutu".split()

    words_dict = map_reduce(
        words, keyfunc=lambda x: x[0], reducefunc=lambda l: sorted(l)
    )

    sorted_list = sorted(words_dict.items())

    groups_mapped = map(lambda x: " ".join(x[1]), sorted_list)

    words_joined = " ".join(groups_mapped)

    print(words_joined)


def ex3():
    numbers = [1, 21, 75, 39, 7, 2, 35, 3, 31, 7, 8]

    numbers_filtered = filter(lambda x: x >= 5, numbers)

    numbers_chunked = chunked(numbers_filtered, 2)

    numbers_multiplied = map(lambda l: l[0] * l[1], numbers_chunked)

    final_sum = reduce(lambda sum, x: sum + x, numbers_multiplied, 0)

    print(final_sum)


if __name__ == "__main__":
    ex2()
    # ex3()
