#!/usr/bin/python3
'''
Remove Dups! Write code to remove duplicates from an unsorted linked list. FOLLOW UP How would you solve this problem if a temporary buffer is not allowed?
'''
import unittest
import logging


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
            self.head = n
        else:
            n = self.head
            while (n.next):
                n = n.next

            logging.debug('New Node added ----> %r', data)
            new_node = Node(data)
            n.next = new_node

    def removeDuplicates(self):
        logging.debug('Removing Duplicates.')
        temp = self.head
        nums = set()
        while temp.next:
            nums.add(temp.data)
            if temp.next.data in nums:
                temp.next = temp.next.next
            temp = temp.next
        logging.debug('Duplicates Removed!---------')

    def removeDuplicatesNoBuffer(self):
        logging.debug('Removing Duplicates - No buffer')
        temp = self.head
        while temp.next:
            second = temp
            while second.next:
                if second.data == second.next.data:
                    second.next = second.next.next
                second = second.next
            temp = temp.next
        logging.debug('Duplicates Removed!----------')

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
        self.link.removeDuplicates()
        self.assertEqual(self.link.toList(), [
            -1,
            4,
            3,
            1,
            20,
            4,
        ])

    def test3(self):
        self.link.addNode(-1)
        self.link.addNode(20)
        self.link.addNode(40)
        self.assertEqual(self.link.toList(), [
            -1,
            4,
            3,
            1,
            20,
            4,
            -1,
            20,
            40,
        ])
        self.link.removeDuplicatesNoBuffer()
        # Note: the duplicates have not been removed.
        self.assertEqual(self.link.toList(), [
            -1,
            4,
            3,
            1,
            20,
            4,
            -1,
            20,
            40,
        ])

    def test4(self):
        self.link.insertHead(-2)
        self.assertEqual(self.link.toList(), [
            -2,
            -1,
            4,
            3,
            1,
            20,
            4,
            -1,
            20,
            40,
        ])


if __name__ == "__main__":
    unittest.main()
