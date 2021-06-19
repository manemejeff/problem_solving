import itertools
from collections import defaultdict
from pprint import pprint

makes = defaultdict(int)

with open('cars_2014.csv') as f:
    next(f)
    make_groups = itertools.groupby(f, key=lambda x: x.split(',')[0])
    make_counts = ((key, len(models)) for key, models in make_groups)
    print(list(make_counts))
data = (
    (1, 'abc'),
    (1, 'bcd'),
    (2, 'pyt'),
    (2, 'yth'),
    (2, 'tho'),
    (3, 'hon')
)

# groups = itertools.groupby(data, key=lambda x: x[0])
# for group_key, sub_iter in groups:
#     print(group_key, list(sub_iter))
#
# def gen_groups():
#     for key in range(1, 4):
#         for i in range(3):
#             yield (key, i)
#