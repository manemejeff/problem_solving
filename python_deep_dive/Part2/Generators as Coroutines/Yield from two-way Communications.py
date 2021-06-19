from inspect import getgeneratorstate, getgeneratorlocals

old = False
new = True


def squares(n):
    for i in range(n):
        yield i ** 2


# def delegator(n):
#     for value in squares(n):
#         yield value
#
# WITHOUT YIELD FROM
# gen = delegator(5)
# for _ in range(5):
#     print(next(gen))

def delegator(n):
    yield from squares(n)


# WITH YIELD FROM
# gen = delegator(5)
# for _ in range(5):
#     print(next(gen))

# caller next --> delegator --> subgen
# subgen yields --> delegator yields --> caller


def song():
    yield "I'm a lumberjack and I'm OK"
    yield "I sleep all night and I work all day"


def play_song():
    count = 0
    s = song()
    yield from s
    yield 'song finished'
    print('player is exiting...')


if old:
    player = play_song()
    print(next(player))
    print(getgeneratorstate(player))
    print(getgeneratorlocals(player))

    s = getgeneratorlocals(player)['s']
    # BOTH GENS ARE SUSPENDED
    print(next(player))
    print(getgeneratorstate(player))
    print(getgeneratorstate(s))
    # S IS CLOSED PLAYER IS SUSPENDED
    print(next(player))
    print(getgeneratorstate(player))
    print(getgeneratorstate(s))
    # GETTING STOPITERATION ECXEPTION
    print(next(player))


def player():
    count = 1
    while True:
        print('Run count:', count)
        yield from song()
        count += 1


if new:
    p = player()
    print(next(p), next(p))
    print(next(p), next(p))
