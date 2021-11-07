def print_items_lin(n):
    """
    Complexity of O(n)
    :param n:
    :return:
    """
    for i in range(n):
        print(i)

def print_items_sq(n):
    """
    Complexity of O(n^2)
    :param n:
    :return:
    """
    for i in range(n):
        for j in range(n):
            print(i, j)