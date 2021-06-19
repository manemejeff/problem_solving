import itertools
from pprint import pprint
from itertools import tee
from fractions import Fraction

def matrix(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            yield f'{i} x {j} = {i*j}'

# pprint(list(itertools.islice(matrix(10), 10, 20)))

l1 = ['x1', 'x2', 'x3', 'x4']
l2 = ['y1', 'y2', 'y3']

# pprint(list(itertools.product(l1, l2)))

def matrix(n):
    for i, j in itertools.product(range(1, n+1), range(1, n+1)):
        yield (i, j, i*j)

# print(list(matrix(4)))

def matrix(n):
    return ((i, j, i*j)
            for i, j in itertools.product(*tee(range(1, n+1), 2)))

# pprint(list(matrix(4)))

def grid(min_val, max_val, step, *, num_dimensions=2):
    axis = itertools.takewhile(lambda x: x <= max_val,
                        itertools.count(min_val, step))
    axes = itertools.tee(axis, num_dimensions)
    return itertools.product(*axes)

# pprint(list(grid(-1, 5, 1)))

sample_space = list(itertools.product(range(1, 7), range(1, 7)))

outcomes = list(filter(lambda x: x[0] + x[1] == 8, sample_space))

odds = Fraction(len(outcomes), len(sample_space))
pprint(odds)