from collections import namedtuple

# PRINTING DOCSTRINGS
Point2D = namedtuple('Point2D', 'x y')
# print(Point2D.__doc__)
# print(Point2D.x.__doc__)
# print(Point2D.y.__doc__)
# print(help(Point2D))

# CHANGING DOCSTRINGS
Point2D.__doc__ = '2D Cartesian coordinate'
Point2D.x.__doc__ = 'x coordinate'
Point2D.y.__doc__ = 'y coordinate'

# print(Point2D.__doc__)
# print(Point2D.x.__doc__)
# print(Point2D.y.__doc__)
# print(help(Point2D))

# DEFAULT VALUES
Vector2D = namedtuple('Vector2D', 'x1 y1 x2 y2 origin_x origin_y')
# PROTOTYPE
vector_zero = Vector2D(0, 0, 0, 0, 0, 0)
v2 = vector_zero._replace(x1=10, y1=10, x2=20, y2=20)
# print(v2)
# MONKEY PATCHING __defaults__
# print(Vector2D.__new__.__defaults__)
Vector2D.__new__.__defaults__ = (10, 10)
v1 = Vector2D(10, 20, 30, 40)
print(v1)