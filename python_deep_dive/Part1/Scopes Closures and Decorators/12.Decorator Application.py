from functools import lru_cache

def timed(fn):
    """

    :param fn:
    :return:
    """
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print('{0}({1}) took {2:.6f}s to run'.format(fn.__name__,
                                                     args_str,
                                                     elapsed))
        return result

    return inner


def timed_avg(fn):
    """

    :param fn:
    :return:
    """
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        elapsed_total = 0
        elapsed_count = 0

        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            elapsed = end - start
            elapsed_total += elapsed
            elapsed_count += 1

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        elapsed_avg = elapsed_total / elapsed_count
        print('{0}({1}) took {2:.6f}s to run'.format(fn.__name__,
                                                     args_str,
                                                     elapsed_avg))
        return result

    return inner


def calc_recurs_fib(n):
    if n <= 2:
        return 1
    else:
        return calc_recurs_fib(n-1) + calc_recurs_fib(n-2)


@timed
def fib_recursive(n):
    return calc_recurs_fib(n)


@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1

    for i in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2

    return fib_2


@timed
def fib_reduce(n):
    from functools import reduce
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]),
                   dummy,
                   initial)
    return fib_n[0]

# recursive took 36 sec
# print(fib_recursive(40))

# loop took 0.000020s
# print(fib_loop(40))

# reduce took 0.000031s
# print(fib_reduce(40))

# DECORATOR APPLICATION (LOGGED, STACKED DECORATORS)


def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called {1}'.format(run_dt, fn.__name__))
        return result

    return inner


@logged
@timed
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))


# print(fact(1000))

# 14 DECORATOR APP (MEMOIZATION)

class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print('Calculating fib({0})...'.format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]

# f = Fib()
#
# print(f.fib(35))


def fib_closure():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            print('Calculating fib({0})...'.format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]

    return calc_fib

# f = fib_closure()
#
# print(f(20))


# V 1.0
def memoize_fib(fib):
    cache = {1: 1, 2: 1}

    def inner(n):
        if n not in cache:
            cache[n] = fib(n)
        return cache[n]

    return inner


# V 2.0
def memoize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner


# @memoize
# def fib_rec(n):
#     print('Calculating fib({0})...'.format(n))
#     return 1 if n < 3 else fib_rec(n-1) + fib_rec(n-2)


@memoize
def factorial(n):
    print('Calculating factorial({0})...'.format(n))
    return 1 if n < 2 else n * factorial(n-1)


# factorial(10)
# factorial(10)
# factorial(20)

@lru_cache()
def fib_rec(n):
    print('Calculating fib({0})...'.format(n))
    return 1 if n < 3 else fib_rec(n-1) + fib_rec(n-2)


print(fib_rec(20))
print('new call')
print(fib_rec(15))