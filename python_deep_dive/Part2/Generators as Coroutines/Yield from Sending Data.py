from inspect import getgeneratorstate, getgeneratorlocals

old = False
new = True


def echo():
    while True:
        received = yield
        print(received[::-1])


if old:
    e = echo()
    next(e)
    e.send('stressed')
    e.send('tons')
    e.close()


def delegator():
    e = echo()
    yield from e


if old:
    d = delegator()
    print(next(d))
    print(getgeneratorlocals(d))
    e = getgeneratorlocals(d)['e']
    print(getgeneratorstate(d))
    print(getgeneratorstate(e))
    d.send('stressed')
    d.send('tons')


def echo():
    output = None
    while True:
        received = yield output
        output = received[::-1]


if old:
    e = echo()
    print(next(e))
    print(e.send('stressed'))


def delegator():
    yield from echo()


if old:
    d = delegator()
    next(d)
    print(d.send('stressed'))

l = [1, 2, [3, 4, [5, 6]], [7, [8, 9, 10]]]


def flatten(curr_item, output):
    if isinstance(curr_item, list):
        for item in curr_item:
            flatten(item, output)
    else:
        output.append(curr_item)


if old:
    output = []
    flatten(l, output)
    print(output)


def flatten_gen(curr_item):
    if isinstance(curr_item, list):
        for item in curr_item:
            yield from flatten_gen(item)
    else:
        yield curr_item


if old:
    for item in flatten_gen(l):
        print(item)


# def is_iterable(item):
#     try:
#         iter(item)
#     except:
#         return False
#     else:
#         return True

# def flatten_gen(curr_item):
#     if is_iterable(curr_item):
#         for item in curr_item:
#             yield from flatten_gen(item)
#     else:
#         yield curr_item


def is_iterable(item, *, str_is_iterable=True):
    try:
        iter(item)
    except:
        return False
    else:
        if isinstance(item, str):
            if str_is_iterable and len(item) > 1:
                return True
            else:
                return False
        else:
            return True


def flatten_gen(curr_item, *, str_is_iterable=True):
    if is_iterable(curr_item, str_is_iterable=str_is_iterable):
        for item in curr_item:
            yield from flatten_gen(item)
    else:
        yield curr_item


if old:
    l = ['abc', [1, 2, (3, 4)]]
    print(list(flatten_gen(l)))


def coro():
    while True:
        received = yield
        print(received)

def gen1():
    yield from gen2()

def gen2():
    yield from gen3()

def gen3():
    yield from coro()

if new:
    g = gen1()
    next(g)
    g.send('hello')