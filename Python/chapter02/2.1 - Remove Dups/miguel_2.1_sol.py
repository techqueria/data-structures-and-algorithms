"""
Python version 3.7.0
2.1 - Remove Dups
Write code to remove duplicates
from an unsorted linked list.
How would you solve this if a temporary
buffer is not allowed?
"""
import unittest


class Node:
    def __init__(self, d: int):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self, *numbers: int):
        self.head = None
        self.tail = None
        for num in numbers:
            self.append_to_tail(num)

    def append_to_tail(self, d: int) -> None:
        if self.head is None:
            self.head = Node(d)
            self.tail = self.head
            return
        end = Node(d)
        self.tail.next = end
        self.tail = end

    def append_to_head(self, d: int) -> None:
        new_head = Node(d)
        new_head.next = self.head
        self.head = new_head

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.head is None:
            return '<empty>'
        ll = []
        n = self.head
        while n.next is not None:
            ll.append('{} -> '.format(n.data))
            n = n.next
        ll.append(str(n.data))
        return ''.join(ll)

    def __eq__(self, other: object):
        if not isinstance(other, LinkedList):
            return NotImplemented
        a = self.head
        b = other.head
        while a is not None and b is not None:
            if a.data != b.data:
                return False
            # otherwise, advance both pointers
            a = a.next
            b = b.next
        return a is None and b is None


def remove_dups(ll: LinkedList) -> LinkedList:
    """
    remove_dups will remove duplicates from the
    input linked list ll. A temporary buffer
    is used.
    Runtime: O(N)
    Space Complexity: O(N)
    :param ll: a linked list
    :return: a linked list without duplicates
    """
    n = ll.head
    unique_vals = {n.data}  # set literal
    output_ll = LinkedList(n.data)
    while n is not None:
        if n.data not in unique_vals:
            output_ll.append_to_tail(n.data)
        unique_vals.add(n.data)
        n = n.next
    return output_ll


def remove_dups_no_buffer(ll: LinkedList) -> LinkedList:
    """
    remove_dups will remove duplicates from the
    input linked list ll. No temporary buffer
    used.
    Runtime: O(N^2)
    Space Complexity: O(1)
    :param ll: a linked list
    :return: a linked list without duplicates
    """
    n = ll.head
    while n is not None:
        curr_data = n.data
        m = n.next
        prev = n
        # search for duplicates from n + 1 to the
        # end of the linked list
        while m is not None:
            if m.data == curr_data:
                # re-arrange pointers to omit
                # the duplicate
                prev.next = m.next
            else:
                # otherwise, advance m and prev pointers
                prev = m
            m = prev.next
        n = n.next
    return ll


class TestRemoveDups(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            (
                LinkedList(*[1, 2, 3, 3, 5]),
                LinkedList(*[1, 2, 3, 5])
            ),
            (
                LinkedList(*[1, 2, 3, 3]),
                LinkedList(*[1, 2, 3])
            ),
            (
                LinkedList(*[1, 2, 2]),
                LinkedList(*[1, 2])
            ),
            (
                LinkedList(*[1]),
                LinkedList(*[1])
            ),
            (
                LinkedList(*[1, 1]),
                LinkedList(*[1])
            ),
            (
                LinkedList(*[2, 2, 2, 2, 2, 2]),
                LinkedList(*[2])
            ),
            (
                LinkedList(*[1, 1, 3, 4, 5, 5, 6, 7]),
                LinkedList(*[1, 3, 4, 5, 6, 7])
            ),
            (
                LinkedList(*[7, 2, 7, 9, 20, 1, 0, 0, 0, 25]),
                LinkedList(*[7, 2, 9, 20, 1, 0, 25])
            ),
            (
                LinkedList(*[9, 8, 7, 6, 6, 1, 2, 3, 4, 4]),
                LinkedList(*[9, 8, 7, 6, 1, 2, 3, 4])
            ),
            (
                LinkedList(*[9, 9, 9, -10, -100, 45, 67, -100, 99]),
                LinkedList(*[9, -10, -100, 45, 67, 99])
            )
        ]

    def test_remove_dups(self):
        for ll, expected in self.test_cases:
            self.assertEqual(remove_dups(ll), expected)

    def test_remove_dups_no_buffer(self):
        for ll, expected in self.test_cases:
            self.assertEqual(remove_dups_no_buffer(ll), expected)


if __name__ == '__main__':
    unittest.main()
