#!/usr/bin/python3

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
        print('Node added to LL--->', data)

    def printList(self):
        if self.head is None:
            print('No LinkedList to print')
            return

        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def partition(self, part):
        '''However, in a linked list, the situation is much easier. Rather than shifting and swapping elements, we can actually create two different linked lists: one for elements less than x, and one for elements greater than or equal to x.'''
        if self.head is None:
            print('No LinkedList to print')
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
        cls.l.printList()
        cls.l.addNode(3)
        cls.l.addNode(20)
        cls.l.addNode(21)
        cls.l.addNode(5)
        cls.l.addNode(8)
        cls.l.addNode(5)
        cls.l.addNode(10)
        cls.l.addNode(2)
        cls.l.addNode(1)
        cls.l.printList()

    @classmethod
    def tearDownClass(cls):
        pass

    def test1(self):
        self.l.partition(5)
        self.l.printList()


if __name__ == '__main__':
    unittest.main()
