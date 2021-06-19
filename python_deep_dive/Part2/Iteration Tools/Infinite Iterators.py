from  itertools import count, cycle, repeat, islice
from decimal import Decimal
from collections import namedtuple
from pprint import pprint

g = count(10)
print(list(islice(g, 5)))

g = count(Decimal('0'), Decimal('0.1'))
print(list(islice(g, 5)))


# CYCLE
g = cycle(('red', 'green', 'blue'))
print(list(islice(g, 5)))

def colors():
    yield 'red'
    yield 'green'
    yield 'blue'

cols = colors()
# print(next(cols))
# print(next(cols))
# print(next(cols))

g = cycle(cols)
print(list(islice(g, 10)))

# EXAMPLE

Card = namedtuple('Card', 'rank suit')

def card_deck():
    ranks = tuple(str(num) for num in range(2, 11)) + tuple('JQKA')
    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    for suit in suits:
        for rank in ranks:
            yield Card(rank, suit)

# print(list(islice(card_deck(), 10)))

hands = [list() for _ in range(4)]

# index = 0
# for card in card_deck():
#     index = index % 4
#     hands[index].append(card)
#     index += 1

# index_cycle = cycle([0, 1, 2, 3])
# for card in card_deck():
#     hands[next(index_cycle)].append(card)

hands_cycle = cycle(hands)
for card in card_deck():
    next(hands_cycle).append(card)

pprint(hands)

# REPEAT

g = repeat('Python')

# for _ in range(10):
#     pprint(next(g))