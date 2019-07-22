"""
Python version 3.7.0
2.7 - Intersection
Given two (singly) linked lists, determine if the two
lists intersect.  Return the intersecting node.
Note that the intersection is defined based on reference,
not value. That is, if the kth node of the first linked
list is the exact same node (by reference) as the jth
node of the second linked list, then they are intersecting.
"""
import unittest
from typing import Optional, NamedTuple


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
        elif isinstance(e, Node):
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

    def _append_node(self, n: Node) -> None:
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
        if self.head is None:
            # if list is empty and we add
            # out first element, head AND tail
            # must point to same node
            self.tail = new_head
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

    def get_value_at(self, index: int) -> int:
        if index < 0 or index >= self.size:
            raise IndexError('list index out of range')
        n = self.head
        for i in range(self.size):
            if i == index:
                return n.data
            n = n.next

    def pop_head(self) -> Node:
        if self.head is None:
            raise IndexError('no head to pop')
        h = self.head
        h.next = None
        self.head = self.head.next
        self.size -= 1
        return h

    def append(self, ll: 'LinkedList') -> None:
        self.tail.next = ll.head
        self.size += ll.size
        ll.head = None
        ll.size = 0

    def reverse(self) -> None:
        """
        Reverses this linked list in place
        :return:
        """
        if self.head is None:
            return
        prev = self.head
        self.tail = prev
        curr = prev.next
        self.tail.next = None
        while curr is not None:
            old_next = curr.next
            curr.next = prev
            prev = curr
            curr = old_next
        self.head = prev

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


def intersection(ll1: LinkedList, ll2: LinkedList) -> Optional[Node]:
    """
    This function will determine if ll1 and ll2 intersect.
    The intersection is defined based on reference, not value.
    Runtime:  O(n^2)
    Space Complexity:  O(1)
    :param ll1: first input linked list
    :param ll2: second input linked list
    :return: The intersecting node or None
    """
    n1 = ll1.head
    while n1 is not None:
        n2 = ll2.head
        while n2 is not None:
            if n1 is n2:
                return n1
            n2 = n2.next
        n1 = n1.next
    return None


class SharedLLStructure(NamedTuple):
    first_segment: LinkedList
    second_segment: LinkedList
    shared_node: Node
    other_list: LinkedList


class TestIntersection(unittest.TestCase):

    def setUp(self):
        shared_structures = [
            SharedLLStructure(
                LinkedList(1, 2, 3),
                LinkedList(5, 10, 11),
                Node(4),
                LinkedList(6, 7, 8, 9)
            ),
            SharedLLStructure(
                LinkedList(1, 2, 3, 4, 5),
                LinkedList(7),
                Node(6),
                LinkedList(9, 8, 7),
            ),
            SharedLLStructure(
                LinkedList(1, 2),
                LinkedList(4, 5),
                Node(3),
                LinkedList(9, 8, 7, 6, 7, 6, 7, 9),
            )
        ]

        self.intersection_test_cases = []

        for ll1_seg1, ll1_seg2, shared_node, ll2 in shared_structures:
            ll1_seg1.append_to_tail(shared_node)
            ll1_seg1.append(ll1_seg2)
            ll2.append_to_tail(shared_node)
            self.intersection_test_cases.append((ll1_seg1, ll2, shared_node))

        self.no_intersection_test_cases = [
            (
                LinkedList(1, 2, 3, 4, 5),
                LinkedList(1, 2, 3)
            ),
            (
                LinkedList(66, 2, 12, 35),
                LinkedList(79, 19, 23, 24)
            ),
            (
                LinkedList(),
                LinkedList(1, 2, 3, 4)
            )
        ]

    def test_intersections(self):
        for ll1, ll2, shared_node in self.intersection_test_cases:
            result_node = intersection(ll1, ll2)
            self.assertTrue(result_node is shared_node, msg=(ll1, ll2, shared_node))

        for ll1, ll2 in self.no_intersection_test_cases:
            self.assertIsNone(intersection(ll1, ll2), msg=(ll1, ll2))


if __name__ == '__main__':
    unittest.main()
