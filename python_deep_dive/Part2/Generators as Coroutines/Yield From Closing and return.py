from inspect import getgeneratorstate, getgeneratorlocals

old = False
new = True

def subgen():
    try:
        while True:
            received = yield
            print(received)
    finally:
        print('subgen: closing...')

def delegator():
    s = subgen()
    yield from s
    yield 'delegator: subgen closed'
    print('delegator closing...')


if old:
    d = delegator()
    next(d)
    print(getgeneratorlocals(d))
    s = getgeneratorlocals(d)['s']
    print(getgeneratorstate(d))
    print(getgeneratorstate(s))
    d.send('hello')
    s.close()
    print(getgeneratorstate(d))
    print(getgeneratorstate(s))
    next(d)
    next(d)

if new:
    d = delegator()
    next(d)
    s = getgeneratorlocals(d)['s']
    print(getgeneratorstate(d))
    print(getgeneratorstate(s))