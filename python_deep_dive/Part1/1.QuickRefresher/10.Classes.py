

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive')
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive')
        else:
            self._height = height

    # def get_width(self):
    #     return self._width
    #
    # def set_width(self, width):
    #     if width <= 0:
    #         raise ValueError('width must be positive.')
    #     else:
    #         self._width = width
    #
    # def get_height(self):
    #     return self._height
    #
    # def set_height(self, height):
    #     if height <= 0:
    #         raise ValueError('height must be positive.')
    #     else:
    #         self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return self._width + self._height

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self._width, self._height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._width
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)

print(r1.__repr__())
print(str(r2))

r1.width = 100
print(r1)

r1.height = -10
print(r1)

print(r1 == r2)