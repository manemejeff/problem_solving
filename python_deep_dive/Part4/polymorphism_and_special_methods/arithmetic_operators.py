from numbers import Real

class Vector:
    def __init__(self, *components):
        if len(components) < 1:
            raise ValueError('Cannot create an empty Vector.')
        for component in components:
            if not isinstance(component, Real):
                raise ValueError(f'Vector components must all be real numbers. {component} is invalid.')
        self._components = tuple(components)

    def __len__(self):
        return len(self._components)

    @property
    def components(self):
        return self._components

    def __repr__(self):
        return f'Vector({self.components})'

    if __name__ == '__main__':
        pass