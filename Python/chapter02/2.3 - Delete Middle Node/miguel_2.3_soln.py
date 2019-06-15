"""
Python version 3.7.0
2.3 - Delete Middle Node
Implement an algorithm to delete a node
in the middle (i.e., any node but the
first and last node, not necessarily
the exact middle) of a singly linked list,
given only access to that node
EXAMPLE
Input:  the node c from the linked list
        a -> b -> c -> d -> e -> f
Result: nothing is returned, but the new
        linked list looks like
        a -> b -> d -> e -> f
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

    def get_node_at(self, index: int) -> Node:
        if index < 0 or index >= self.size:
            raise IndexError('list index out of range')
        n = self.head
        i = 0
        while n is not None:
            if i == index:
                return n
            i += 1
            n = n.next

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


def delete_middle_node(ll: LinkedList, node: Node) -> LinkedList:
    """
    delete_middle_node will delete a node from
    a singly linked list. The node can be any
    node within the linked list that is NOT the
    head or the tail.
    We will be comparing the address of
    the input node with the address of each
    node in the linked list.
    Runtime: O(N)
    Space Complexity: O(1)
    :param ll: an input linked list
    :param node: pointer to a node in ll
    :return: a linked list with/wo having deleted node
    """
    if node is ll.head or node is ll.tail:
        raise ValueError('node cannot be head or tail of linked list')
    n = ll.head
    while n.next is not None:
        if n.next is node:
            n.next = n.next.next
        n = n.next
    return ll


class TestDeleteMiddleNode(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            (
                LinkedList(1, 2, 3, 4, 5, 6),
                2,
                LinkedList(1, 2, 4, 5, 6),
            ),
            (
                LinkedList(3, 6, 2, 1, 7, 8),
                1,
                LinkedList(3, 2, 1, 7, 8),
            ),
            (
                LinkedList(-100, 200, 65, 22, 1),
                3,
                LinkedList(-100, 200, 65, 1),
            )
        ]

    def test_delete_middle_node(self):
        for ll, node_index, expected in self.test_cases:
            result = delete_middle_node(ll, ll.get_node_at(node_index))
            self.assertEqual(result, expected, msg=(ll, node_index, expected))

    def test_delete_middle_node_value_error(self):
        ll = LinkedList(1, 2, 3, 4)
        head = ll.head
        tail = ll.tail
        with self.assertRaises(ValueError, msg=(ll, ll.head)):
            delete_middle_node(ll, head)
        with self.assertRaises(ValueError, msg=(ll, ll.tail)):
            delete_middle_node(ll, tail)


if __name__ == '__main__':
    unittest.main()
