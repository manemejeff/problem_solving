# exercise 1
composers = {
    'Johann': 65,
    'Ludwig': 56,
    'Frederic': 39,
    'Wolfgang': 35
}

# print(dict(sorted(composers.items(), key=lambda x: x[1])))

# EX 2

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}


def common_keys(d1: dict, d2: dict) -> dict:
    keys: set = d1.keys() & d2.keys()
    d = {key: (d1[key], d2[key]) for key in keys}
    return d


# print(common_keys(d1, d2))

# EX 3

d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}


def combine_dicts(*dicts):
    uns: dict = {}
    for d in dicts:
        for k, v in d.items():
            uns[k] = uns.get(k, 0) + v

    return dict(sorted(uns.items(), key=lambda x: x[1], reverse=True))


# print(combine_dicts(d1, d2, d3))

# EX 4

n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}

def not_all(node1: dict, node2: dict, node3: dict):
    union = node1.keys() | node2.keys() | node3.keys()

    intersection = node1.keys() & node2.keys() & node3.keys()
    relevant = union - intersection
    result = {
        key: (node1.get(key, 0), node2.get(key, 0), node3.get(key, 0))
        for key in relevant
    }
    return result


print(not_all(n1, n2, n3))