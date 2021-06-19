from collections import namedtuple
import numbers

class Point:
    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = (x, y)
        else:
            raise TypeError('Point co-ordinates must be real numbers.')

    def __repr__(self):
        return f'Point(x={self._pt[0]}, y={self._pt[1]})'

    def __len__(self):
        return len(self._pt)

    def __getitem__(self, item):
        # METHOD PROVIDES UNPACKING, INDEXING, SLICING - BY DELEGATING IT TO A TUPLE
        return self._pt[item]


class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, item):
        return self._pts[item]

    def __setitem__(self, s, value):
        try:
            rhs = [Point(*pt) for pt in value]
            is_single = True
        except TypeError:
            try:
                rhs = Point(*value)
                is_single = False
            except TypeError:
                raise TypeError('Invalid Point or iterable of Points')
        if (isinstance(s, int) and is_single) or (isinstance(s, slice) and not is_single):
            self._pts[s] = rhs
        else:
            raise TypeError('Incompatible index/slice assignment.')

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('Can only concatenate with another Polygon')

    def __delitem__(self, index):
        del self._pts[index]

    def pop(self, i):
        return self._pts.pop(i)

    def append(self, pt):
        self._pts.append(Point(*pt))

    def insert(self, i, pt):
        self._pts.insert(i, Point(*pt))

    def extend(self, pts):
        if isinstance(pts, Polygon):
            self._pts += pts._pts
        else:
            points = [Point(*pt) for pt in pts]
            self._pts += points

    def __iadd__(self, other):
        self.extend(other)
        return self


p1 = Polygon((0, 0), (1, 1))
p2 = Polygon((2, 2), (3, 3))
print(id(p1), id(p2))
print(p1)
p1 += p2
print(id(p1))
print(p1)

p1.append([10, 10])
print(p1, 'APPEND')
p1.insert(1, Point(-1, -1))
print(p1, 'INSERT')
p1.extend(p2)
print(p1, 'EXTEND')


