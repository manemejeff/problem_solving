from collections import namedtuple

Point2D = namedtuple('Point2D', 'x y')

pt = Point2D(10, 20)
print(pt)

# we can use previous inst for creating new
pt = Point2D(100, pt.y)
print(pt)
# ----------------------------------------------------------------
# USING UNPACKING
Stock = namedtuple('Stock', 'symbol year month day open high low close')
djia  = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
print(djia)
# unpacking values from tuple except last one which we gonna change
*values, _ = djia
# print(values)
# values += [26_393]
values.append(26_393)
djia = Stock(*values)
# ----------------------------------------------------------------
# USING SLICING
values = djia[:7]
# values += (100,)
# djia = Stock(*(values + (100,)))
djia = Stock(*values, 1000)
# print(values)
# ----------------------------------------------------------------
# USING REPLACE
djia = djia._replace(year=2019, open=10000)
# USING MAKE
# djia = Stock._make(values + (100,))
# ----------------------------------------------------------------
# CREATING NEW INSTANCES BASED ON OTHERS
# Point2D._fields + ('z',)
Point3D = namedtuple('Point3D', Point2D._fields + ('z',))
StockExt = namedtuple('StockExt', Stock._fields + ('previous_close',))
pt = Point2D(100, 20)
pt3d = Point3D(*pt, 50)
# print(pt3d)

print(help(Point2D))