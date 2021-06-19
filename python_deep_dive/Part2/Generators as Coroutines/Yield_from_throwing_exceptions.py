old = False
new = True


class CloseCoroutine(Exception):
    pass


def echo():
    try:
        while True:
            received = yield
            print(received)
    except CloseCoroutine:
        return 'coro was closed'
    except GeneratorExit:
        print('closed method was called/or GeneratorExit thrown')


if old:
    e = echo()
    next(e)
    # EXCEPTION TROWN
    # e.throw(CloseCoroutine)

    # EXCEPTION SILENCED
    # e.close()

    # EXCEPTION THROWN
    # e.throw(GeneratorExit)


def delegator():
    result = yield from echo()
    yield 'subgen closed and returned:', result
    print('delegator closing...')


if old:
    d = delegator()
    next(d)
    d.send('hello')
    print(d.throw(CloseCoroutine))


class IgnoreMe(Exception):
    pass


def echo():
    try:
        while True:
            try:
                received = yield
                print(received)
            except IgnoreMe:
                yield "I'm ignoring you!"
    except CloseCoroutine:
        return 'coro was closed'
    except GeneratorExit:
        print('closed method was called/or GeneratorExit thrown')

if old:
    d = delegator()
    next(d)
    d.send('python')
    result = d.throw(IgnoreMe, 1000)
    print(result)


def echo():
    output = None
    try:
        while True:
            try:
                received = yield output
                print(received)
            except IgnoreMe:
                output = "I'm ignoring you!"
            else:
                output = None
    except CloseCoroutine:
        return 'coro was closed'
    except GeneratorExit:
        print('closed method was called/or GeneratorExit thrown')


if old:
    d = delegator()
    next(d)
    d.send('python')
    print(d.throw(IgnoreMe))
    d.send('rocks')


def delegator():
    try:
        yield from echo()
    except ValueError:
        print('delegator got the value error')

if old:
    d = delegator()
    next(d)
    d.throw(ValueError)

def delegator():
    while True:
        try:
            yield from echo()
        except ValueError:
            print('delegator got the value error')


if old:
    d = delegator()
    d.__next__()
    d.send('python')
    d.throw(ValueError)
    d.send('rocks')
    d.throw(IgnoreMe)


class WriteAverage(Exception):
    pass


def averager(out_file):
    total = 0
    count = 0
    average = None
    with open(out_file, 'w') as f:
        f.write('count,average\n')
        while True:
            try:
                received = yield average
                total += received
                count += 1
                average = total/count
            except WriteAverage:
                if average is not None:
                    print('saving average to file:', average)
                    f.write(f'{count}, {average}\n')


if new:
    avg = averager('sample.csv')
    next(avg)
    avg.send(1)
    print(avg.send(2))
    avg.throw(WriteAverage)
    avg.send(3)
    avg.send(2)
    avg.throw(WriteAverage)
    avg.close()