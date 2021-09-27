from time import perf_counter


class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count


# Closure realization

def averager():
    total = 0
    count = 0

    def add(number):
        nonlocal total
        nonlocal count
        total += number
        count += 1
        return total / count

    return add


# Timer class realization

class Timer:
    def __init__(self):
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start


# Timer closure realization

def timer():
    start = perf_counter()

    def poll():
        return perf_counter() - start

    return poll


# t2 = timer()
# print(t2())
# print(t2())

# PART 2

# def counter(initial_value=0):
#
#     def inc(increment=1):
#         nonlocal initial_value
#         initial_value += increment
#         return initial_value
#
#     return inc

# v.1.0

# def counter(fn):
#     cnt = 0
#
#     def inner(*args, **kwargs):
#         nonlocal cnt
#         cnt += 1
#         print('{0} has been called {1} times.'.format(fn.__name__, cnt))
#         return fn(*args, **kwargs)
#
#     return inner

# for storing in global variable
# counters = dict()

def counter(fn, counters):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)

    return inner


def add(a, b):
    return a + b


def mult(a, b):
    return a * b


counter_add = counter(add)
print(counter_add(5, 5))
print(counter_add.__closure__)
print(counter_add.__code__.co_freevars)
print(counter_add(100, 5000))