from functional import seq


data = input("baga sirul: ")

result = (
    seq(list(data))
    .map(lambda c: (c, 1))
    .reduce_by_key(lambda x, y: 0)
    .map(lambda t: t[0])
    .make_string("")
)

print(result)
