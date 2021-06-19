class CyclicIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
        # self.length = length

    def __iter__(self):
        return self

    def __next__(self):
        result = self.lst[self.i % len(self.lst)]
        self.i += 1
        return result

    # FOR FINITE ITERS WITH LENGTH
    # def __next__(self):
    #     if self.i >= self.length:
    #         raise StopIteration
    #     else:
    #         result = self.lst[self.i % len(self.lst)]
    #         self.i += 1
    #         return result


numbers = range(10)
iter_cycl = CyclicIterator('NSWE')
print(list(zip(list(numbers), iter_cycl)))