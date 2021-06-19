import math

new = True
old = False

def coroutine(coro):
    def inner(*args, **kwargs):
        gen = coro(*args, **kwargs)
        next(gen)
        return gen
    return inner


@coroutine
def handle_data():
    while True:
        received = yield
        print(received)


@coroutine
def power_up(n, next_gen):
    while True:
        received = yield
        output = math.pow(received, n)
        next_gen.send(output)

if old:
    print_data = handle_data()
    gen2 = power_up(3, print_data)
    gen1 = power_up(2, gen2)
    for i in range(1, 6):
        gen1.send(i)


@coroutine
def filter_even(next_gen):
    while True:
        received = yield
        if received % 2 == 0:
            next_gen.send(received)


if new:
    print_data = handle_data()
    filtered = filter_even(print_data)
    gen2 = power_up(3, filtered)
    gen1 = power_up(2, gen2)
    for i in range(1, 6):
        gen1.send(i)