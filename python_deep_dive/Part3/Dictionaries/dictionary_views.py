
new = True
old = False

s1 = {1, 2, 3}
s2 = {2, 3, 4}

if old:
    print(s1 | s2)
    print(s1 & s2)
    print(s1 - s2)

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'a': 10, 'b': 20, 'c': 30, 'e': 5}

if new:
    union = d1.keys() | d2.keys()
    intersection = d1.keys() & d2.keys()
    keys = union - intersection
    # print(d1.keys() ^ d2.keys())

    # result = {}
    # # for key in keys:
    # #     result[key] = d1.get(key) or d2.get(key)
    # # print(result)

    results = {key: d1.get(key) or d2.get(key) for key in d1.keys() ^ d2.keys()}
    print(results)