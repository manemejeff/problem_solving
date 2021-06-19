import math


class FactIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            result = math.factorial(self.i)
            self.i += 1
            return result


fact_iter = FactIter(3)
print(list(fact_iter))
print(list(fact_iter))


def fact():
    i = 0

    def inner():
        nonlocal i
        result = math.factorial(i)
        i += 1
        return result

    return inner

fact_iter = iter(fact(), math.factorial(5))

def my_func():
    # print('line 1')
    yield 'Flying'
    # print('line 2')
    yield 'Circus'

f = my_func()
print(type(f))

for res in f:
    print(res)