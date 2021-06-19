# CUSTOM SEQUENCE PART 1

class Silly:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        print('called __len__')
        return self.n

    def __getitem__(self, item):
        # TO DIFFER INDEXES FROM SLICES
        print(type(item))

        print(f'you requested item item at {item}')
        if item < 0 or item >= self.n:
            raise IndexError
        else:
            return 'This is a silly element'

from functools import lru_cache


class Fib:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if isinstance(item, int):
            if item < 0 or item >= self.n:
                raise IndexError
            else:
                return Fib._fib(item)
        else:
            start, stop, step = item.indices(self.n)
            rng = range(start, stop, step)
            return [Fib._fib(i) for i in rng]

    @staticmethod
    @lru_cache(2 ** 10)
    def _fib(n):
        if n < 2:
            return 1
        else:
            return Fib._fib(n - 1) + Fib._fib(n - 2)


# silly = Silly(10)
# print(len(silly))

f = Fib(15)
print(f[0], f[7])
print(list(f))
print(f[0:5])