import itertools
from pprint import pprint
from collections import namedtuple
from fractions import Fraction

l1 = 'abc'

# pprint(list(itertools.permutations(l1)))
# pprint(list(itertools.permutations(l1, 2)))

# pprint(list(itertools.combinations([1, 2, 3, 4], 2)))
# pprint(list(itertools.combinations_with_replacement([1, 2, 3, 4], 2)))

SUITS = 'SHDC'
RANKS = tuple(map(str, range(2, 11))) + tuple('JQKA')

# deck = [rank + suit for suit in SUITS for rank in RANKS]
# deck = [rank + suit for suit, rank in itertools.product(SUITS, RANKS)]

Card = namedtuple('Card', 'rank suit')

# deck = [Card(rank, suit) for suit, rank in itertools.product(SUITS, RANKS)]
deck = (Card(rank, suit) for suit, rank in itertools.product(SUITS, RANKS))

sample_space = itertools.combinations(deck, 4)
total = 0
acceptable = 0

# USING FOR LOOP
# for outcome in sample_space:
#     total += 1
#     for card in outcome:
#         if card.rank != 'A':
#             break
#     else:
#         acceptable += 1


for outcome in sample_space:
    total += 1
    if all(map(lambda x: x.rank == 'A', outcome)):
        acceptable += 1


pprint(f'total={total}, acceptable={acceptable}')
pprint('odds = {}'.format(Fraction(acceptable, total)))
pprint('odds = {:.10f}'.format(acceptable/total))