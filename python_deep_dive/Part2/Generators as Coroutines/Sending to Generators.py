from inspect import getgeneratorstate

def echo():
    while True:
        received = yield
        print('You said:', received)

# e = echo()
# print(getgeneratorstate(e))
# next(e)
# print(getgeneratorstate(e))
# e.send('python')

def running_averager():
    total = 0
    count = 0
    running_average = None
    while True:
        value = yield running_average
        total += value
        count += 1
        running_average = total / count

def running_averages(iterable):
    averager = running_averager()
    next(averager)
    for value in iterable:
        running_average = averager.send(value)
        print(running_average)

print(running_averages([1, 2, 3, 4]))