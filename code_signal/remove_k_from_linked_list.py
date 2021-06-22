"""
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example

    For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
    removeKFromList(l, k) = [1, 2, 4, 5];
    For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
    removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7].

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] linkedlist.integer l

    A singly linked list of integers.

    Guaranteed constraints:
    0 ≤ list size ≤ 105,
    -1000 ≤ element value ≤ 1000.

    [input] integer k

    An integer.

    Guaranteed constraints:
    -1000 ≤ k ≤ 1000.

    [output] linkedlist.integer

    Return l with all the values equal to k removed.

"""


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    if l is not None:
        while l is not None and l.value == k:
            l = l.next

        tmp_node = l
        while tmp_node is not None and tmp_node.next is not None:
            if tmp_node.next.value == k:
                tmp_node.next = tmp_node.next.next
            else:
                tmp_node = tmp_node.next

    return l
