def fact(n):
    """
    Factorial function

    :param n:
    :return:
    """
    return 1 if n < 2 else n * fact(n - 1)

# MAP

# map creates objects with functions which calculated when iterated
# getting list from fact function applied to range 6
# results = list(map(fact, range(6)))
# --------------------------------------------------


l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
l3 = 100, 200, 300, 400

# sum function applied to 2 lists
results = list(map(lambda x, y: x + y, l1, l2))
print(results)

# get the error when iterates through this map object bcs function have 2 arguments, but we applied it to 3 objects
# results = map(lambda x, y: x + y, l1, l2, l3))
# -----------------------------------------------

# FILTER

x = range(25)
# get list of numbers divideble by 3
print(list(filter(lambda x: x % 3 == 0, x)))

# get truthy elements from list (None for some reason works that way)
print(list(filter(None, [1, 0, 4, 'a', '', None, True, False])))

# ZIP

l1 = [1, 2, 3, 4]
l2 = [10, 20 , 30, 40]
l3 = 'python'

# zip creates tuples from each list element given
print(list(zip(l1, l2, l3)))

#  LIST COMPREHENSION

# [] - creates list with results of fact function
results = [fact(n) for n in range(10)]
print(results)

# () - creates generator object
# generator iterated only once
results = (fact(n) for n in range(10))
print(results)

print(list(map(lambda x, y: x+y, l1, l2)))
print([x+y for x, y in zip(l1, l2)])

print(list(filter(lambda x: x % 2 == 0, map(lambda x, y: x+y, l1, l2))))
print([x+y for x, y in zip(l1, l2) if (x+y)%2 == 0])