from functools import wraps


def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        """
        This is inner closure
        :param args:
        :param kwargs:
        :return:
        """
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)

    inner = wraps(fn)(inner)
    return inner

def add (a: int, b: int):
    """
    adds two values

    :param a:
    :param b:
    :return:
    """
    return a + b


def mult(a: int, b: int = 1):
    """
    Multiplies the values

    :param a:
    :param b:
    :return:
    """
    return a * b


print(help(add))
add = counter(add)
print(help(add))