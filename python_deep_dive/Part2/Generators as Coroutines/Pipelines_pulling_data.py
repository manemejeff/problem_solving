import csv
import itertools

new = True
old = False

# WITHOUT CONTEXT MANAGER
# def parse_data(f_name):
#     f = open(f_name)
#     try:
#         dialect = csv.Sniffer().sniff(f.read(2000))
#         f.seek(0)
#         next(f) # skip header row
#         yield from csv.reader(f, dialect=dialect)
#     finally:
#         f.close()

def parse_data(f_name):
    with open(f_name) as f:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        next(f)
        yield from csv.reader(f, dialect=dialect)


def filter_data(rows, contains):
    for row in rows:
        if contains in row[0]:
            yield row


# caller <-- filter <-- data

if old:
    data = parse_data('cars.csv')
    filtered_1 = filter_data(data, 'Chevrolet')
    filtered_2 = filter_data(filtered_1, 'Carlo')

    for row in filtered_2:
        print(row)


def output(f_name):
    data = parse_data(f_name)
    filter_1 = filter_data(data, 'Chevrolet')
    filter_2 = filter_data(filter_1, 'Carlo')
    yield from filter_2


if old:
    results = output('cars.csv')
    for row in results:
        print(row)


def output(f_name, *filter_words):
    data = parse_data(f_name)
    for filter_word in filter_words:
        data = filter_data(data, filter_word)
    yield from data

if new:
    results = output('cars.csv', 'Chevrolet', 'Carlo', 'Landau')
    for row in results:
        print(row)