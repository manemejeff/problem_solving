from itertools import filterfalse, compress, takewhile, dropwhile
from math import sin, pi

# itertools.
# filterfalse
# compress
# takewhile
# dropwhile

def cubes(n):
    for i in range(n):
        print(f'yilding {i}')
        yield i**3

def is_odd(x):
    return x % 2 == 1

def is_even(x):
    return x % 2 == 0

# filtered = filter(is_odd, cubes(10))
# print(list(filtered))
#
# filtered = filterfalse(is_odd, cubes(10))
# print(list(filtered))

def sine_wave(n):
    start = 0
    max_ = 2 * pi
    step = (max_ - start) / (n - 1)

    for _ in range(n):
        yield round(sin(start), 2)
        start += step

# print(list(sine_wave(15)))
# print(list(takewhile(lambda x: 0 <= x <= 0.9, sine_wave(15))))
#
# l = [1, 3, 5, 2, 1]
# print(list(dropwhile(lambda x: x < 5, l)))

data = ['a', 'b', 'c', 'd', 'e']
selectors = [True, False, 1, 0]

print(list(zip(data, selectors)))

comp = [item for item, truth_value in zip(data, selectors) if truth_value]
print(comp)

comp = list(compress(data, selectors))
print(comp)