class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0

    def __len__(self):
        return self.length

    def __next__(self):
        print('__next__ called')
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

    def __iter__(self):
        print('__iter__ called')
        return self

if __name__ == '__main__':
    sq = Squares(5)
    l = [(item, item + 1) for item in sq]
    print(l)
    print(l)
