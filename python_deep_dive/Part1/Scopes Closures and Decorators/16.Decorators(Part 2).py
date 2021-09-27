def timed(reps):
    def dec(fn):
        from time import perf_counter

        def inner(*args, **kwargs):

            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)

            avg_run_time = total_elapsed / reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
            return result
        return inner
    return dec


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)

@timed(25)
def fib(n):
    return calc_fib_recurse(n)


def dec_factory(a, b):
    print('Running dec factory')

    def dec(fn):
        print('Renning dec')

        def inner(*args, **kwargs):
            print('Running inner')
            print('a={0}, b={1}'.format(a, b))
            return fn(*args, **kwargs)

        return inner
    return dec

@dec_factory(100, 200)
def my_func():
    print('Running my_func')

fib(12)
# my_func()