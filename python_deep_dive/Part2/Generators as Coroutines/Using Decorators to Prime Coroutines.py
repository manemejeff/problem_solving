from inspect import getgeneratorstate
import math

def coroutine(gen_fn):
    def inner():
        gen = gen_fn()
        next(gen)
        return gen
    return inner

@coroutine
def echo():
    while True:
        received = yield
        print(received)

# echo = coroutine(echo)
# e = echo()
# print(getgeneratorstate(e))

# e = echo()
# e.send('hello')

def coroutine(gen_fn):
    def inner(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        next(gen)
        return gen
    return inner

@coroutine
def power_up(p):
    result = None
    while True:
        received = yield result
        result = math.pow(received, p)

# squares = power_up(2)
# cubes = power_up(3)
#
# print(squares.send(2))
# print(cubes.send(3))

@coroutine
def power_up(p):
    result = None
    while True:
        received = yield result
        try:
            result = math.pow(received, p)
        except TypeError:
            result = None

squares = power_up(2)
print(squares.send(2))