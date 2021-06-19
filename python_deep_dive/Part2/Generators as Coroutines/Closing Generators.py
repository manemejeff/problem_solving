from inspect import getgeneratorstate
import csv
import itertools

def parse_file(f_name):
    print('opening file...')
    f = open(f_name, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        reader = csv.reader(f, dialect=dialect)
        for row in reader:
            yield row
    finally:
        print('closing file...')
        f.close()

# parser = parse_file('cars.csv')
# for row in itertools.islice(parser, 10):
#     print(row)
# parser.close()

class TransactionAborted(Exception):
    pass

def save_to_db():
    print('starting new transaction')
    is_abort = False
    try:
        while True:
            data = yield
            print('sending data to database', eval(data))
    except Exception as ex:
        is_abort = True
        raise TransactionAborted(str(ex))
    finally:
        if is_abort:
            print('rollback transaction')
        else:
            print('commit transaction')

trans = save_to_db()
next(trans)
trans.send('1 + 10')
trans.send('1/0')
trans.close()