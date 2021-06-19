from numbers import Number

def squares(n):
    for i in range(n):
        yield i**2

list(squares(5))

class Person:
    def __bool__(self):
        return True

    def __len__(self):
        return 0

print(bool(Person))

class MySeq:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        pass

def is_numeric(v):
    return isinstance(v, Number)

l = [10, 20, 30, 40, 0]

pred_l = map(is_numeric, l)
print(list(pred_l))
pred_l = (is_numeric(item) for item in l)
print(all(pred_l))

l = [10, 20, 30, 40, 'hello']
print(all(map(lambda x: isinstance(x, Number), l)))
