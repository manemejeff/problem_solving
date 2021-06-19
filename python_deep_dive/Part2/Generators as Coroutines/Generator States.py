from inspect import getgeneratorstate
def gen(s):
    for c in s:
        yield c

g = gen('abc')

print(getgeneratorstate(g))
print(next(g))
print(getgeneratorstate(g))
print(list(g))
print(getgeneratorstate(g))