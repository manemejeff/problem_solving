def my_gen():
    try:
        print('Creating context')
        yield [1, 2, 3, 4]
    finally:
        print('Exiting context')

# gen = my_gen()

class GenCtxManager:
    def __init__(self, gen_func, *args, **kwargs):
        self._gen = gen_func(*args, **kwargs)

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False

# with GenCtxManager(my_gen) as obj:
#     print(obj)

def open_file(fname, mode):
    f = open(fname, mode)
    try:
        print('opening file')
        yield f
    finally:
        print('closing file')
        f.close()

with GenCtxManager(open_file, 'text.txt', 'r') as f:
    print(f.readlines())