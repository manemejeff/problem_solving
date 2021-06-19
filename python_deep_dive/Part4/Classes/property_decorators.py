def my_decorator(fn):
    # print('decorating fumction')
    def inner(*args, **kwargs):
        print('running decorated function')
        return fn(*args, **kwargs)
    return inner

def undecorated_function(a, b):
    print('running original function')
    return a + b

# decorated_func = my_decorator(undecorated_function)
# print(decorated_func(1, 2))

@my_decorator
def my_func(a, b):
    print('running original function')
    return a + b

class Person:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        print('getter called')
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

if True:
    p = Person('John')
    print(p.name)