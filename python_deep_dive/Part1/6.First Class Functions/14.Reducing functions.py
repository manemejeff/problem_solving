from functools import reduce

l = [5, 8, 6, 10, 9]

_max = lambda x, y: x if x > y else y


def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result


print(max_sequence(l))

_min = lambda a, b: a if a < b else b


def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result


print(min_sequence(l))

_add = lambda a, b: a + b


def add_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result, x)
    return result


print(add_sequence(l))


def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result


print(_reduce(_max, l))
print(_reduce(_min, l))
print(_reduce(_add, l))

s1 = {False, 0, '', None, 1}
print(all(s1))
print(any(s1))

rd = reduce(lambda a, b: bool(a) and bool(b), s1)
print(rd)
rd = reduce(lambda a, b: bool(a) or bool(b), s1)
print(rd)

def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

print(fact(7))