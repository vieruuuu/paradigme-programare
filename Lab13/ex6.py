from functional import seq


data = input("baga sirul: ")

result = (
    seq(list(data))
    .map(lambda c: (c, 1))
    .reduce_by_key(lambda x, y: x + y)
    .map(lambda t: t[0] + str(t[1]) if t[1] > 1 else t[0])
    .make_string("")
)

print(result)
