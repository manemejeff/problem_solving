import time


def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()

    for i in range(rep):
        fn(args, kwargs)

    end = time.perf_counter()
    return (end - start) / rep

def compute_powers(n, *, start=1, end):
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results
