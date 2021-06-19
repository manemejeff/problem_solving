import random

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(l)

rnd = sorted(l, key=lambda elem: random.random())

print(rnd)
