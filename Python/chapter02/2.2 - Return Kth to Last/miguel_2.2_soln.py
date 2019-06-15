"""
Python version 3.7.0
2.2 - Return Kth to Last
Implement an algorithm to find the kth
to last element of a singly linked list
Example:
    input: ll = a -> b -> c -> d -> e -> f
            k = 3
    output: d because d is 3rd to last
"""
import unittest


class Node:
    def __init__(self, d: int):
        self.data = d
        self.next = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '<Node Value: {}>'.format(self.data)

    def __eq__(self, other: object):
        if not isinstance(other, Node):
            return NotImplemented
        return self.data == other.data


class LinkedList:
    def __init__(self, *numbers: int):
        self.head = None
        self.tail = None
        self.size = 0
        for num in numbers:
            self.append_to_tail(num)

    def append_to_tail(self, d: int) -> None:
        if self.head is None:
            self.head = Node(d)
            self.tail = self.head
        else:
            end = Node(d)
            self.tail.next = end
            self.tail = end
        self.size += 1

    def append_to_head(self, d: int) -> None:
        new_head = Node(d)
        new_head.next = self.head
        self.head = new_head
        self.size += 1

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


def kth_to_last(ll: LinkedList, k: int) -> Node:
    """
    kth_to_last will return the kth to last node
    from the input linked list.
    Going to reverse the linked list and then
    count k steps.
    Runtime: O(N)
    Space Complexity: O(1)
    :param ll: a linked list
    :param k:
        an integer where k > 0 and k < ll size
    :return:
        kth to last Node from the linked list
        or None
    """
    if k <= 0 or k > ll.size:
        raise IndexError('list index out of range')
    # go size - k steps
    n = ll.head
    i = 1
    while n is not None and i <= ll.size - k:
        n = n.next
        i += 1
    return n


class TestKthToLast(unittest.TestCase):

    def test_kth_to_last(self):
        l = list(range(1, 6))
        ll = LinkedList(*l)
        for k in range(1, len(l)):
            self.assertEqual(kth_to_last(ll, k), Node(l[-k]), msg=(ll, l[-k]))

    def test_kth_to_last_index_error(self):
        k_values = [-1, 7, 0]
        ll = LinkedList(1, 2, 3)
        for k in k_values:
            with self.assertRaises(IndexError, msg=(ll, k)):
                kth_to_last(ll, k)


if __name__ == '__main__':
    unittest.main()
