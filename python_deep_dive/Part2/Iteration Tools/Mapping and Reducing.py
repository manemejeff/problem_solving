from itertools import starmap, accumulate, chain
from functools import reduce
import operator
# MAPPING AND REDUCING

maps = map(lambda x: x**2, range(5))
# maps is iterator

print(reduce(lambda x, y: x * y, [1, 2, 3, 4], 10))

def sum_(iterable):
    it = iter(iterable)
    acc = next(it)
    yield acc
    for item in it:
        acc += item
        yield acc

# for item in sum_([10, 20, 30]):
#     print(item)

def running_reduce(fn, iterable, start=None):
    it = iter(iterable)
    if start is None:
        acc = next(it)
    else:
        acc = start
    yield acc
    for item in it:
        acc = fn(acc, item)
        yield acc

# print(list(running_reduce(operator.add, [10, 20, 30])))

print(list(accumulate([10, 20, 30], operator.mul)))