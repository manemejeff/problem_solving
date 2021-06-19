t = 10, 3, 5, 8, 6, 1, 4

print(sorted(t))

l = 'this bird is a late parrot'.split(' ')

print(l)
# FUNCTION sorted RETURNS NEW OBJECT
print(sorted(l, key=lambda s: len(s)))
# METHOD sort IS INPLACE SORT
l.sort(key=lambda s:len(s))
print(l)