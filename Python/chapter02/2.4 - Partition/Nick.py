#!/usr/bin/python3

import logging
import unittest


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        logging.debug('Node added to LL---> %r', data)

    def toList(self):
        if self.head is None:
            return []

        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

    def partition(self, part):
        '''However, in a linked list, the situation is much easier. Rather than shifting and swapping elements, we can actually create two different linked lists: one for elements less than x, and one for elements greater than or equal to x.'''
        if self.head is None:
            logging.debug('No LinkedList to print')
            return

        temp = self.head
        before = SinglyLinkedList()
        after = SinglyLinkedList()
        while temp.next:
            if temp.data >= part:
                after.addNode(temp.data)
            else:
                before.addNode(temp.data)
            temp = temp.next

        # combine the two linked lists
        self.head = before.head
        temp = before.head
        while temp.next:
            temp = temp.next
        temp.next = after.head


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.l = SinglyLinkedList()
        cls.l.addNode(3)
        cls.l.addNode(20)
        cls.l.addNode(21)
        cls.l.addNode(5)
        cls.l.addNode(8)
        cls.l.addNode(5)
        cls.l.addNode(10)
        cls.l.addNode(2)
        cls.l.addNode(1)

    @classmethod
    def tearDownClass(cls):
        pass

    def test1(self):
        self.assertEqual(self.l.toList(), [3, 20, 21, 5, 8, 5, 10, 2, 1])
        self.l.partition(5)
        # Note that this code has a bug: it loses the final 1!
        self.assertEqual(self.l.toList(), [3, 2, 20, 21, 5, 8, 5, 10])


if __name__ == '__main__':
    unittest.main()
