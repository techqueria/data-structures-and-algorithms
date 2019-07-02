"""
Python version 3.7.0
2.5 - Sum Lists
You have two numbers represented by a linked list,
where each node contains a single digit.
The digits are stored in reverse order, such that
the 1's digit is at the head of the list.  Write a
function that adds the two numbers and returns the sum
as a linked list.
EXAMPLE
Input:  (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295
Result: 2 -> 1 -> 9. That is, 912
FOLLOW UP
Suppose the digits are stored in forward order.
Repeat the above problem.
EXAMPLE
Input:  (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295
Result: 9 -> 1 -> 2. That is, 912
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


def sum_lists_forward(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    """
    Will add ll1 and ll2 where each element in the linked lists
    represent digits.
    Precondition: ll1 and ll2 must be the same length.
    Digits are in forward order, for example:
    Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295
    Output: 9 -> 1 -> 2. That is, 912
    Runtime: O(n)
    Space Complexity: O(n) - output_ll
    :param ll1: first input linked list
    :param ll2: second input linked list
    :return: a linked list containing the result of the addition
    """
    assert(ll1.size == ll2.size)
    n1 = ll1.head
    n2 = ll2.head
    output_ll = LinkedList()
    prev_node = None
    while n1 is not None:
        first = n1.data
        second = n2.data
        result = first + second
        if result >= 10:
            carry = 1
            result -= 10  # extract digit in one's place
            if prev_node is None:
                # for when the first addition yields a carry
                # and the output linked list is empty
                output_ll.append_to_head(carry)
            else:
                # add carry to previous digit
                prev_node.data += carry
        output_ll.append_to_tail(result)
        n1 = n1.next
        n2 = n2.next
        prev_node = output_ll.tail

    # if carry > 0:
    #     output_ll.append_to_tail(carry)
    return output_ll


def sum_lists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    """
    Will add ll1 and ll2 where each element in the linked lists
    represent digits.
    Precondition: ll1 and ll2 must be the same length.
    Digits are in backward order, for example:
    Input:  (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295
    Result: 2 -> 1 -> 9. That is, 912
    Runtime: O(n)
    Space Complexity: O(n) - output_ll
    :param ll1: first input linked list
    :param ll2: second input linked list
    :return: a linked list containing the result of the addition
    """
    assert(ll1.size == ll2.size)
    n1 = ll1.head
    n2 = ll2.head
    output_ll = LinkedList()
    carry = 0
    while n1 is not None:
        first = n1.data
        second = n2.data
        result = first + second + carry
        if result >= 10:
            carry = 1
            result -= 10  # extract digit in one's place
        else:
            carry = 0
        output_ll.append_to_tail(result)
        n1 = n1.next
        n2 = n2.next
    if carry > 0:
        output_ll.append_to_tail(carry)
    return output_ll


class TestSumLists(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            (
                LinkedList(7, 1, 6),
                LinkedList(5, 9, 2),
                LinkedList(2, 1, 9)
            ),
            (
                LinkedList(1, 1, 1, 1),
                LinkedList(2, 2, 2, 2),
                LinkedList(3, 3, 3, 3)
            ),
            (
                LinkedList(5),
                LinkedList(4),
                LinkedList(9)
            ),
            (
                LinkedList(5),
                LinkedList(6),
                LinkedList(1, 1)
            ),
            (
                LinkedList(7, 1, 9),
                LinkedList(5, 9, 2),
                LinkedList(2, 1, 2, 1)
            ),
            (
                LinkedList(9, 9, 9, 9),
                LinkedList(9, 9, 9, 9),
                LinkedList(8, 9, 9, 9, 1)
            )
        ]

        self.forward_test_cases = [
            (
                LinkedList(6, 1, 7),
                LinkedList(2, 9, 5),
                LinkedList(9, 1, 2)
            ),
            (
                LinkedList(1, 1, 1, 1),
                LinkedList(2, 2, 2, 2),
                LinkedList(3, 3, 3, 3)
            ),
            (
                LinkedList(3),
                LinkedList(2),
                LinkedList(5)
            ),
            (
                LinkedList(5),
                LinkedList(6),
                LinkedList(1, 1)
            ),
            (
                LinkedList(9, 9, 9, 9),
                LinkedList(9, 9, 9, 9),
                LinkedList(1, 9, 9, 9, 8)
            )
        ]

    def test_sum_lists_forward_order(self):
        for ll1, ll2, expected in self.forward_test_cases:
            self.assertEqual(sum_lists_forward(ll1, ll2), expected, msg=(ll1, ll2))

    def test_sum_lists(self):
        for ll1, ll2, expected in self.test_cases:
            self.assertEqual(sum_lists(ll1, ll2), expected, msg=(ll1, ll2))


if __name__ == '__main__':
    unittest.main()
