# class MyClass:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'MyClass(name={self.name})'
#
#     def __add__(self, other):
#         print(f'You called + on {self} and {other}')
#         return 'Hello from __add__'
#
#     def __iadd__(self, other):
#         print(f'You called += on {self} and {other}')
#         return 'Hello from __iadd__'
#
# c1 = MyClass('instance 1')
# c2 = MyClass('instance 2')
#
# THE FIRST VERSION THE ID IS CHANGING BUT IT SHOULD NOT
# print(c1 + c2, id(c1))
# c1 += c2
# print(c1, id(c1))


class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass(name={self.name})'

    def __add__(self, other):
        return MyClass(self.name + other.name)

    def __iadd__(self, other):
        if isinstance(other, MyClass):
            self.name += other.name
        else:
            self.name += other
        return self

    def __mul__(self, n):
        return MyClass(self.name * n)

    def __rmul__(self, n):
        return self.__mul__(n)

    def __imul__(self, n):
        self.name *= n
        return self

    def __contains__(self, value):
        return value in self.name

c1 = MyClass('Neuro')
c2 = MyClass('Father')
# CONCATENATION WITH __add__ METHOD
result = c1 + c2
print(result, id(c1))
# INPLACE CONCATENATION WITH __iadd__ METHOD
c1 += c2
print(c1, id(c1))
# MULTIPLICATION WITH __mul__ METHOD
result = c2 * 3
print(result, id(result))
# INPLACE MULTIPLICATION WITH __imul__ METHOD
c2 *= 3
print(c2, id(c2))
# __contains__ METHOD
print('Father' in c2)
