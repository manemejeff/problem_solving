# This Class could be replaced with named tuple
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z})'

    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

from collections import namedtuple

def dot_product_3d(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z


def dot_product(a, b):
    return sum(e[0] * e[1] for e in zip(a, b))

# Point2D = namedtuple('Point2D', ['x', 'y'])
# pt1 = Point2D(10, 20)
# print(pt1)
# pt1 = Point3D(1, 2, 3)
# pt2 = Point3D(1, 1, 1)
# print(dot_product_3d(pt1, pt2))
#
# a = (1, 2)
# b = (1, 1)
# print(list(zip(a, b)))
# print(sum(e[0] * e[1] for e in zip(a, b)))

Circle = namedtuple('Circle', 'center_x center_y     radius')
c = Circle(0, 0, 10)
print(c)
Stock = namedtuple('Stock', '''symbol
                            year
                            month
                            day
                            open
                            high
                            low
                            close''')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
print(djia._fields)

