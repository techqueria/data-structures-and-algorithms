"""
Python version 3.7.0
2.4 - Partition
Write code to partition a linked list around a value x,
such that all nodes less than x come before all nodes
greater than or equal to x. If x is contained within
the list, the values of x only need to be after
the elements less than x. The partition element x
can appear anywhere in the 'right partition'; it does
not need to appear between the left and right
partitions.
EXAMPLE
Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [pivot = 5]
Result: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
import unittest
from typing import Optional


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

    def append_to_tail(self, e) -> None:
        if isinstance(e, int):
            self._append_num(e)
        elif isinstance(e, Node) or e is None:
            self._append_node(e)

    def _append_num(self, d: int) -> None:
        if self.head is None:
            self.head = Node(d)
            self.tail = self.head
        else:
            end = Node(d)
            self.tail.next = end
            self.tail = end
        self.size += 1

    def _append_node(self, n: Optional[Node] = None) -> None:
        if self.head is None:
            self.head = n
            self.tail = self.head
        else:
            end = n
            self.tail.next = end
            self.tail = end
        self.size += 1

    def append_to_head(self, d: int) -> None:
        new_head = Node(d)
        new_head.next = self.head
        self.head = new_head
        self.size += 1

    def get_node_at(self, index: int) -> Node:
        if index < 0 or index >= self.size:
            raise IndexError('list index out of range')
        n = self.head
        for i in range(self.size):
            if i == index:
                return n
            n = n.next

    def pop_head(self) -> Optional[Node]:
        if self.head is None:
            return self.head
        h = self.head
        self.head = self.head.next
        return h

    def append(self, ll: object):
        if not isinstance(ll, LinkedList):
            return TypeError
        self.tail.next = ll.head

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


def check_partitioned(ll: LinkedList, pivot: int) -> bool:
    """
    Will check if a linked list is partitioned
    around a value such that all values less
    then the partition value come before all values
    greater than or equal to the partition value
    in the linked list.
    Order doesn't matter, as long as the values
    < partition come before values >= partition.
    Runtime: O(n)
    Space Complexity: O(1)
    :param ll: an input linked list
    :param pivot: a number to partition around
    :return:
    """
    # counter for keeping track of how many times
    # we change from < pivot to >= pivot
    n = ll.head
    while n is not None:
        if n.data >= pivot:
            break
        n = n.next
    while n is not None:
        if n.data < pivot:
            return False
        n = n.next
    return True


def partition_ll(ll: LinkedList, pivot: int) -> LinkedList:
    """
    This function will take in a linked list, a
    pivot value, and will partition a linked
    list around a value x such that all nodes
    less than x come before all nodes greater than
    or equal to x.  If x is in the list, then
    the value(s) of x only need to be after the
    elements less than x. They do not need to appear
    in between the left and right partitions.
    Runtime: O(n)
    Space Complexity: O(1)
    :param ll: an input linked list
    :param pivot: a number to partition around
    :return: a linked list that is 'partitioned'
    """
    left_partition = LinkedList()  # will contain values < pivot
    right_partition = LinkedList()  # will contain values >= pivot

    n = ll.head
    while n is not None:
        if n.data < pivot:
            left_partition.append_to_tail(ll.pop_head())
        else:
            right_partition.append_to_tail(ll.pop_head())
        n = n.next
    # last element may still be pointing
    # to earlier elements that are less than
    # pivot so we need to cut that link
    right_partition.append_to_tail(ll.pop_head())
    # then, merge left and right partition lists into one linked list
    left_partition.append(right_partition)
    return left_partition


class TestPartition(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            (
                LinkedList(3, 5, 8, 5, 10, 2, 1),
                5
            ),
            (
                LinkedList(1, 2, 3, 4, 5, 6, 7, 8),
                5
            ),
            (
                LinkedList(1, 9, 2, 5, 20, 11, 12),
                10
            ),
            (
                LinkedList(1),
                200
            )
        ]

        self.check_partitioned_test_cases = [
            (
                LinkedList(3, 2, 1, 5, 8, 5, 10),
                5,
                True
            ),
            (
                LinkedList(3, 1, 2, 10, 5, 5, 8),
                5,
                True
            ),
            (
                LinkedList(3, 5, 8, 5, 10, 2, 1),
                5,
                False
            ),
            (
                LinkedList(10, 9, 8, 3, 2, 200, 201),
                5,
                False
            ),
            (
                LinkedList(5, 6, 7, 8, 9, 10),
                5,
                True
            ),
            (
                LinkedList(10),
                5,
                True
            ),
            (
                LinkedList(10, 9, 8, 7, 6, 5, 4, 3, 2, 1),
                1,
                True
            ),
            (
                LinkedList(10, 9, 8, 7, 6, 5, 4, 3, 2, 1),
                5,
                False
            ),
            (
                LinkedList(1, 2, 3, 4, 5, 6, 7, 8, 9),
                5,
                True
            ),
            (
                LinkedList(5, 1),
                5,
                False
            ),
        ]

    def test_check_partitioned(self):
        for ll, pivot, output in self.check_partitioned_test_cases:
            self.assertEqual(check_partitioned(ll, pivot), output, msg=(ll, pivot))

    def test_partition(self):
        for ll, pivot in self.test_cases:
            partitioned_ll = partition_ll(ll, pivot)
            self.assertTrue(check_partitioned(partitioned_ll, pivot), msg=(ll, pivot))


if __name__ == '__main__':
    unittest.main()
