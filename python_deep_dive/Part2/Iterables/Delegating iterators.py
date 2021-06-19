from collections import namedtuple

Person = namedtuple('Person', 'first last')

class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [person.first.capitalize() + ' ' + person.last.capitalize()
                             for person in persons]
        except(TypeError, AttributeError):
            self._persons = []

    def __iter__(self):
        return iter(self._persons)

persons = [Person('michaeL', 'paLin'), Person('eric', 'idle'), Person('John', 'cLeese')]

persons_names = PersonNames(persons)
print(persons_names._persons)

for name in persons_names:
    print(name)