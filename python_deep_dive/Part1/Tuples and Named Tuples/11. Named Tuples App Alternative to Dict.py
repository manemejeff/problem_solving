from collections import namedtuple

data_dict = dict(key1=100, key2=200, key3=300)
Data = namedtuple('Data', data_dict.keys())
d1 = Data(*data_dict.values())
# print(d1)
d2 = Data(**data_dict)
# print(d2)

# GETTING ATTRS
key_name = 'key2'
print(data_dict[key_name])
print(getattr(d2, key_name))

data_list = [
    {'key2': 2, 'key1': 1},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]

keys = {key for dict_ in data_list for key in dict_.keys()}

Struct = namedtuple('Struct', sorted(keys))
Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)

tuple_list = []
for dict_ in data_list:
    tuple_list.append(Struct(**dict_))

print(tuple_list)


def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', sorted(keys))
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]