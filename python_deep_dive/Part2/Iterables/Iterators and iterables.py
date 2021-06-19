class Cities:
    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']
        self._index = 0

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        print('Cities __iter__ called')
        return self.CityIterator(self)
    
    def __getitem__(self, item):
        print('getting item')
        return self._cities[item]

    class CityIterator:
        def __init__(self, city_obj):
            print('CityIterator new object')
            self._city_obj = city_obj
            self._index = 0

        def __iter__(self):
            print('CityIterator __iter__ called')
            return self

        def __next__(self):
            print('CityIterator __next__ called')
            if self._index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities(self._index)
                self._index += 1
                return item

