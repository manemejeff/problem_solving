from datetime import datetime
from random import choice, seed


class TimeUTC:
    def __get__(self, instance, owner):
        return datetime.utcnow().isoformat()


class Logger:
    current_time = TimeUTC()


# class Deck:
#
#     @property
#     def suit(self):
#         return choice(('Spade', 'Heart', 'Diamond', 'Club'))
#
#     @property
#     def card(self):
#         return choice(tuple('23456789JQKA') + ('10',))

class Choice:
    def __init__(self, *choices):
        self.choices = choices

    def __get__(self, instance, owner):
        return choice(self.choices)


class Deck:
    suit = Choice('Spade', 'Heart', 'Diamond', 'Club')
    card = Choice(*'23456789JQKA', '10')


class Dice:
    die_1 = Choice(1, 2, 3, 4, 5, 6)
    die_2 = Choice(1, 2, 3, 4, 5, 6)
    die_3 = Choice(1, 2, 3, 4, 5, 6)


# class StrProp:
#     def __get__(self, instance, owner):
#         if instance is None:
#             return 'Default'
#         else:


class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

if __name__ == '__main__':
    # print(Logger.current_time)
    # l = Logger()
    # print(l.current_time)

    seed(0)

    # d = Deck()
    # for _ in range(10):
    #     print(d.card, d.suit)

    dice = Dice()
    for _ in range(10):
        print(dice.die_1, dice.die_2, dice.die_3)
