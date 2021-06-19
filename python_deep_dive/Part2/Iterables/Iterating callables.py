class CallableIterator:
    def __init__(self, callable_, sentinel):
        self.callable_ = callable_
        self.sentinel = sentinel
        self.is_consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_consumed:
            raise StopIteration
        else:
            result = self.callable_()
            if result == self.sentinel:
                self.is_consumed = True
                raise StopIteration
            else:
                return result


import random

# random.seed(0)
# for i in range(10):
#     print(i, random.randint(0, 10))

random_iter = iter(lambda : random.randint(0, 10), 8)
# random.seed(0)
for num in random_iter:
    print(num)