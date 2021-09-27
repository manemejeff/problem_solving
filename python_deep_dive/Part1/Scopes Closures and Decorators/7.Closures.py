def outer():
    x = [1, 2, 3]
    print(hex(id(x)))

    def inner():
        y = x
        print(hex(id(y)))

    return inner

