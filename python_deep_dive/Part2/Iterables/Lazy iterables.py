import math

class Circle:
    def __init__(self, r):
        self.radius = r
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area is None:
            print('Calculating area')
            self._area = math.pi * (self.radius ** 2)
        return self._area

class Factorial:
    # DONT NEED INIT BCS DONT NEED TO BE FINITE
    # def __init__(self, length):
    #     self.length = length

    def __iter__(self):
        # return self.FactIter(self.length)
        return self.FactIter()

    class FactIter:
        def __init__(self):
            # self.length = length
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            # if self.i >= self.length:
            #     raise StopIteration
            # else:
            result = math.factorial(self.i)
            self.i += 1
            return result