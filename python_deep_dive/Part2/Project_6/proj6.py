import csv


def prime_it(fn):
    def inner(*args, **kwargs):
        g = fn(*args, **kwargs)
        next(g)
        return g

    return inner


def data_reader(f_name):
    with open(f_name, 'r') as f:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        reader = csv.reader(f, dialect=dialect)
        yield from reader


if __name__ == '__main__':
    for row in data_reader('cars.csv'):
        print(row)
