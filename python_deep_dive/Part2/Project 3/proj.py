from collections import namedtuple
from datetime import datetime
from functools import partial

file_name = 'nyc_parking_tickets_extract.csv'
with open(file_name) as f:
    column_headers = next(f).strip('\n').split(',')
    # sample_data = next(f).strip('\n').split(',')

column_names = [header.replace(' ', '_').lower() for header in column_headers]

Ticket = namedtuple('Ticket', column_names)

with open(file_name) as f:
    next(f)
    raw_data_row = next(f)


def read_data():
    with open(file_name) as f:
        next(f)
        yield from f


def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default


def parse_date(value, *, default=None):
    date_format = '%m/&d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default


def parse_string(value, *, default=None):
    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        else:
            return cleaned
    except ValueError:
        return default


column_parsers = (parse_int,
                  parse_string,
                  lambda x: parse_string(x, default=''),
                  partial(parse_string, default=''),
                  parse_date,
                  parse_int,
                  partial(parse_string, default=''),
                  parse_string,
                  lambda x: parse_string(x, default='')
                  )

def parse_row(row, *, default=None):
    fields = row.strip('\n').split(',')
    parsed_data = (func(field) for func, field in zip(column_parsers, fields))
    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    else:
        return default

rows = read_data()
for _ in range(5):
    row = next(rows)
    parsed_data = parse_row(row)
    print(parsed_data)