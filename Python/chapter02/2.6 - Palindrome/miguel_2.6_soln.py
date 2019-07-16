"""
Python version 3.7.0
2.6 - Palindrome
Implement a function to check if a linked list
is a palindrome.

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


def reverse_linked_list(ll: LinkedList) -> LinkedList:
    """
    Takes in a linked list and returns a reversed copy
    :param ll: input linked list
    :return: reversed linked list
    """
    output_ll = LinkedList()
    n = ll.head
    while n is not None:
        output_ll.append_to_head(n.data)
        n = n.next
    return output_ll


def palindrome(ll: LinkedList) -> bool:
    """
    Given a linked list, this function will check if the
    linked list is a palindrome.
    A palindrome is a word or phrase that is the same
    forwards and backwards.
    Since I will use integer nodes for the linked list,
    we will be checking if the sequence of numbers
    in a linked list is a palindrome.
    Runtime:  O(n)
    Space Complexity:  O(n)
    :param ll: an input linked list
    :return: true if ll is a palindrome, false otherwise
    """
    return ll == reverse_linked_list(ll)


class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            (
                LinkedList(1, 2, 3, 4, 3, 2, 1),
                True
            ),
            (
                LinkedList(1, 2, 3, 2, 1),
                True
            ),
            (
                LinkedList(1, 2, 3, 4, 2, 1),
                False
            ),
            (
                LinkedList(4, 5, 6, 7, 8, 9),
                False
            ),
            (
                LinkedList(99, 0),
                False
            ),
            (
                LinkedList(100, 100),
                True
            ),
            (
                LinkedList(7),
                True
            ),
            (
                LinkedList(),
                True
            )
        ]

    def test_palindrome(self):
        for ll, expected in self.test_cases:
            self.assertEqual(palindrome(ll), expected, msg=ll)


if __name__ == '__main__':
    unittest.main()
