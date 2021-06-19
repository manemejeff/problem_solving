from html import escape
from decimal import Decimal


def html_escape(arg):
    return escape(str(arg))


def html_int(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))


def html_real(a):
    return '{0:.2f}'.format(round(a, 2))


def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')


def html_list(l):
    items = ('<li>{0}</li>'.format(htmlize(item))
             for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(html_escape(k), htmlize(v))
             for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_set(arg):
    return html_list(arg)


# print(html_str("""this is
# a multiline string
# with special characters 10 < 100"""))
#
# print(html_int(255))

def htmlize(arg):
    registry = {
        object: html_escape,
        int: html_int,
        float: html_real,
        Decimal: html_real,
        str: html_str,
        list: html_list,
        tuple: html_list,
        set: html_set,
        dict: html_dict,
    }
    # OLD CODE NOT HOW YOU SHOULD DO IT
    # if isinstance(arg, int):
    #     return html_int(arg)
    # elif isinstance(arg, float) or isinstance(arg, Decimal):
    #     return html_real(arg)
    # elif isinstance(arg, str):
    #     return html_str(arg)
    # elif isinstance(arg, list) or isinstance(arg, tuple):
    #     return html_list(arg)
    # elif isinstance(arg, dict):
    #     return html_dict(arg)
    # elif isinstance(arg, set):
    #     return html_set(arg)
    # else:
    #     return html_escape(arg)

    fn = registry.get(type(arg), registry[object])
    return fn(arg)


def singledispatch(fn):
    registry = {}

    registry[object] = fn

    # OLD
    # registry[int] = lambda a: '{0}(<i>{1}</i>)'.format(a, str(hex(a)))
    # registry[str] = lambda s: escape(s).replace('\n', '<br/>\n')

    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)

    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn

        return inner

    def dispatch(type_):
        return registry.get(type_, registry[object])
    decorated.register = register
    # decorated.registry = registry
    decorated.dispatch = dispatch
    return decorated


@singledispatch
def htmlize(a):
    return escape(str(a))


# print(htmlize.registry)


@htmlize.register(int)
def html_int(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))


# print(htmlize.registry)


@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(htmlize(item))
             for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


# print(htmlize.registry)
# print(htmlize(100))
# print(htmlize(["""Python
# rocks! 0 < 1
# """, (10, 20, 30), 100]))

# PART 3 -------------------------------------------

from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence

@singledispatch
def htmlize(a):
    return escape(str(a))


@htmlize.register(Integral)
def htmlize_integral_number(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))


@htmlize.register(Sequence)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(htmlize(item))
             for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


@htmlize.register(tuple)
def html_tuple(t):
    items = (escape(str(item)) for item in t)
    return '({0})'.format(', '.join(items))

print(htmlize((1, 2, 3)))
