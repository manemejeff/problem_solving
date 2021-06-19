import math

old = False
new = True

# FIRST METHOD
a = {'k1': 100, 'k2': 200}

if old:
    print(hash((1, 2, 3)))


def my_func(a, b, c):
    print(a, b, c)


if old:
    print(hash(my_func))
    d = {my_func: [10, 20, 30]}


def fn_add(a, b):
    return a + b


def fn_inv(a):
    return 1 / a


def fn_mult(a, b):
    return a * b


if old:
    funcs = {fn_add: (10, 20), fn_inv: (2,), fn_mult: (2, 8)}
    for f in funcs:
        print(f)

    # for f in funcs:
    #     result = f(*funcs[f])
    #     print(result)

    for f, args in funcs.items():
        print(f(*args))

# SECOND METHOD
d = dict([('a', 100), ['x', 200]])

# ANOTHER ONE
if old:
    keys = ['a', 'b', 'c']
    values = (1, 2, 3)

    d = {}
    for k, v in zip(keys, values):
        d[k] = v

    d2 = {k: v for k, v in zip(keys, values)}

if old:
    keys = 'abcd'
    values = range(1, 5)

    d = {k: v for k, v in zip(keys, values) if v % 2 == 0}
    print(d)

# ANOTHER ONE COMPREHENSION
if old:
    x_coords = (-2, -1, 0, 1, 2)
    y_coords = (-2, -1, 0, 1, 2)

    grid = [(x, y)
            for x in x_coords
            for y in y_coords
            ]
    print(grid)

    # grid_extended = [(x, y, math.hypot(x, y)) for x, y in grid]
    grid_extended = {(x, y): math.hypot(x, y) for x, y in grid}
    print(grid_extended)

if new:
    counters = dict.fromkeys(['a', 'b', 'c'], 0)
    counters = dict.fromkeys('abc', 0)
    d = dict.fromkeys('python')