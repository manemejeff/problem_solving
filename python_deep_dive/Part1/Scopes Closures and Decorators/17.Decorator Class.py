def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('Decorated function called: a={0}, b={1}'.format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec

@my_dec(10, 20)
def my_func(s):
    print('Hello {0}'.format(s))


my_func(69)

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print('Decorated function called: a={0}, b={1}'.format(self.a, self.b))
            return fn(*args, **kwargs)

        return inner

@MyClass(66, 99)
def my_func(s):
    print('Hello {0}'.format(s))

my_func('world')