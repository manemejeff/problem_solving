"""
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers, determine whether or not it's a palindrome.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example

    For l = [0, 1, 0], the output should be
    isListPalindrome(l) = true;

    For l = [1, 2, 2, 3], the output should be
    isListPalindrome(l) = false.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] linkedlist.integer l

    A singly linked list of integers.

    Guaranteed constraints:
    0 ≤ list size ≤ 5 · 105,
    -109 ≤ element value ≤ 109.

    [output] boolean

    Return true if l is a palindrome, otherwise return false.

"""


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def linked_list_reverse(head):
    # Reversing a linked list
    prev = None
    while head is not None:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev


def isListPalindrome(l):
    slow = l
    fast = l

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    slow = linked_list_reverse(slow)
    fast = l

    while slow is not None:
        if slow.value != fast.value:
            return False
        slow = slow.next
        fast = fast.next

    return True
