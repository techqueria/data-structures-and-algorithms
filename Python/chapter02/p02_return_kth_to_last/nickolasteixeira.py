#!/usr/bin/python3
'''
Return Kth to Last: Implement an algorithm to
find the kth to last element of a singly linked list.
'''

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
        self.size = 0

    def insertHead(self, data):
        logging.debug('Inserting head!-----> %r', data)
        n = Node(data)
        temp = self.head
        self.head = n
        self.head.next = temp

    def addNode(self, data):
        if not self.head:
            n = Node(data)
            logging.debug('New Head added ----> %r', data)
            self.head = n
        else:
            n = self.head
            while (n.next):
                n = n.next

            logging.debug('New Node added ----> %r', data)
            new_node = Node(data)
            n.next = new_node

    def kthToLastElement(self, num):
        if num < 1:
            logging.debug('Must be a positive number')
            return None

        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next

        if num > length:
            logging.debug('Input number cannot be larger than number of nodes')
            return None
        else:
            temp = self.head
            for x in range(length - num):
                temp = temp.next

            return temp.data

    def toList(self):
        n = self.head

        result = []
        while(n):
            result.append(n.data)
            n = n.next
        return result


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.link = SinglyLinkedList()
        cls.link.addNode(-1)
        cls.link.addNode(-1)
        cls.link.addNode(4)
        cls.link.addNode(3)
        cls.link.addNode(4)
        cls.link.addNode(1)
        cls.link.addNode(20)
        cls.link.addNode(4)
        cls.link.addNode(4)

    @classmethod
    def tearDownClass(cls):
        logging.debug('---Teardown successful---')

    def test1(self):
        self.assertEqual(self.link.toList(), [
            -1,
            -1,
            4,
            3,
            4,
            1,
            20,
            4,
            4,
        ])

    def test2(self):
        self.assertEqual(self.link.kthToLastElement(0), None)
        self.assertEqual(self.link.kthToLastElement(1), 4)
        self.assertEqual(self.link.kthToLastElement(2), 4)
        self.assertEqual(self.link.kthToLastElement(3), 20)
        self.assertEqual(self.link.kthToLastElement(9), -1)
        self.assertEqual(self.link.kthToLastElement(10), None)


if __name__ == "__main__":
    unittest.main()
