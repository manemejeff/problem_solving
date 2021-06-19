import csv
from contextlib import contextmanager

new = True
old = False


def data_reader(f_name):
    with open(f_name, 'r') as f:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        reader = csv.reader(f, dialect=dialect)
        yield from reader


if old:
    for row in data_reader('car_data.csv'):
        print(row)

input_file = 'car_data.csv'

idx_make = 0
idx_model = 1
idx_year = 2
idx_vin = 3
idx_color = 4

headers = ['make', 'model', 'year', 'vin', 'color']

converters = (str, str, int, str, str)


def data_parser():
    data = data_reader(input_file)
    next(data)
    for row in data:
        parsed_row = [converter(item)
                      for converter, item in zip(converters, row)]
        yield parsed_row


if old:
    data = data_parser()
    for _ in range(5):
        print(next(data))


def coroutine(fn):
    def inner(*args, **kwargs):
        g = fn(*args, **kwargs)
        next(g)
        return g

    return inner


@coroutine
def save_data(f_name, headers):
    with open(f_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        while True:
            data_row = yield
            writer.writerow(data_row)


@coroutine
def filter_data(filter_predicate, target):
    while True:
        data_row = yield
        if filter_predicate(data_row):
            target.send(data_row)


@coroutine
def broadcast(targets):
    while True:
        data_row = yield
        for target in targets:
            target.send(data_row)


def process_data():
    out_pink = save_data('pink_cars.csv', headers)
    out_ford_green = save_data('ford_green.csv', headers)
    out_older = save_data('older.csv', headers)

    filter_pink_cars = filter_data(lambda d: d[idx_color].lower() == 'pink',
                                   out_pink)

    def pred_ford_green(d):
        return (d[idx_make].lower() == 'ford'
                and d[idx_color].lower() == 'green')

    filter_ford_green = filter_data(pred_ford_green, out_ford_green)
    filter_old = filter_data(lambda d: d[idx_year] <= 2010, out_older)
    filters = (filter_pink_cars, filter_ford_green, filter_old)

    broadcaster = broadcast(filters)

    for row in data_parser():
        broadcaster.send(row)

    print('finished processing.')


if old:
    process_data()

@coroutine
def pipeline_coro():
    out_pink = save_data('pink_cars.csv', headers)
    out_ford_green = save_data('ford_green.csv', headers)
    out_older = save_data('older.csv', headers)

    filter_pink_cars = filter_data(lambda d: d[idx_color].lower() == 'pink',
                                   out_pink)

    def pred_ford_green(d):
        return (d[idx_make].lower() == 'ford'
                and d[idx_color].lower() == 'green')

    filter_ford_green = filter_data(pred_ford_green, out_ford_green)
    filter_old = filter_data(lambda d: d[idx_year] <= 2010, out_older)
    filters = (filter_pink_cars, filter_ford_green, filter_old)

    broadcaster = broadcast(filters)

    while True:
        row = yield
        broadcaster.send(row)


if old:
    pipe = pipeline_coro()
    data = data_parser()
    for row in data:
        pipe.send(row)
    pipe.close()


@contextmanager
def pipeline():
    p = pipeline_coro()
    try:
        yield p
    finally:
        p.close()


if new:
    with pipeline() as pipe:
        data = data_parser()
        for row in data:
            pipe.send(row)