r = range(10)
print('__next__' in dir(r))
# RANGE RETURNS ITERABLE

z = zip([1, 2, 3], 'abc')
print('__next__' in dir(z))
# ZIP RETURNS ITERATOR

f = open('cars.csv')
f.close()
# OPEN RETURNS ITERATOR

e = enumerate('Python rocks')
print(iter(e) is e)
# ENUMERATE RETURNS ITERATOR