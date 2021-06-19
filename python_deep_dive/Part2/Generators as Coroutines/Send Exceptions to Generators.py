
def gen():
    while True:
        try:
            received = yield
            print(received)
        except ValueError as ex:
            print('Value error received:', str(ex))
# g = gen()
# next(g)
# g.send('hello')
# g.throw(ValueError, 'custom message')

class CommitException(Exception):
    pass

class RollbackException(Exception):
    pass

def write_to_db():
    print('opening database connection')
    print('start transaction...')
    try:
        while True:
            try:
                data = yield
                print('writing data to database...', data)
            except CommitException:
                print('commiting transaction...')
                print('opening next transaction...')
            except RollbackException:
                print('aborting transaction')
                print('opening next transaction...')
    finally:
        print('generator closing...')
        print('abort transaction...')
        print('closing database connection...')

sql = write_to_db()
next(sql)
sql.send(100)
sql.throw(CommitException)