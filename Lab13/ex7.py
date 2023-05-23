from itertools import starmap
from functools import partial

f = lambda x, k: x * x + k


def partial_method(l: list[int], k: int) -> list[int]:
    func = partial(f, k=k)

    result = map(func, l)

    return list(result)


def starmap_method(l: list[int], k: int) -> list[int]:
    data = map(lambda x: (x, k), l)

    result = starmap(f, data)

    return list(result)


l = [1, 2, 3, 4, 5, 6]

print(partial_method(l, 2))


print(starmap_method(l, 2))
