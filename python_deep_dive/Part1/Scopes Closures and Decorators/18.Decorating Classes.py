from fractions import Fraction
from datetime import datetime, timezone

# BASIC EXAMPLES
# f = Fraction(2, 3)
# Fraction.is_integral = lambda self: self.denominator == 1
# f1 = Fraction(64, 8)
# print(f1.is_integral())

# MONKEY PATCHING DECORATOR
def dec_speak(cls):
    cls.speak = lambda self, message: "{0} says: {1}".format(
        self.__class__.__name__,
        message)

    return cls

# Fraction = dec_speak(Fraction)
# f1 = Fraction(2, 3)
# print(f1.speak('Hello'))

class Person:
    pass

# Person = dec_speak(Person)
# p = Person()
# print(p.speak('this works'))


def info(self):
    results = []
    results.append('time: {0}'.format(datetime.now(timezone.utc)))
    results.append('id: {0}'.format(hex(id(self))))
    results.append('Class: {0}'.format(self.__class__.__name__))
    for k, v in vars(self).items():
        results.append('{0}: {1}'.format(k, v))
    return results


def debug_info(cls):
    cls.debug = info
    return cls

@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi(self):
        return 'Hello there!'


# Longer version of decoration with closure
# Person = debug_info(Person)

# Decorating a class
# p = Person('John', 1939)
# print(p.debug())

@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError(f'Speed cannot exceed top_speed {self.top_speed}.')
        else:
            self._speed = new_speed


# favorite = Automobile('Ford', 'Model T', 1908, 45)
# print(favorite.debug())
# favorite.speed = 40
# print(favorite.debug())

from math import sqrt
from functools import total_ordering

# Bad code
# Do not monkey patch the dunder methods
def complete_ordering(cls):
    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not(self < other) and not (self == other)
        cls.__ge__ = lambda self, other: not(self < other)
    return cls

@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented




p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)
print(abs(p1))
print(p1 == p2)
print(p1 <= p3)
print(p2 >= p1)
print(p1 != p2)


