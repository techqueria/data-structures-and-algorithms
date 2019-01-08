#!/usr/bin/python3
'''
Return Kth to Last: Implement an algorithm to
find the kth to last element of a singly linked list.
'''
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
        print('Inserting head!----->', data)
        n = Node(data)
        temp = self.head
        self.head = n
        self.head.next = temp

    def addNode(self, data):
        if not self.head:
            n = Node(data)
            print('New Head added ---->', data)
            self.head = n
        else:
            n = self.head
            while (n.next):
                n = n.next

            print('New Node added ---->', data)
            new_node = Node(data)
            n.next = new_node

    def kthToLastElement(self, num):
        if num < 1:
            print('Must be a positive number')
            return

        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next

        if num > length:
            print('Input number cannot be larger than number of nodes')
        else:
            temp = self.head
            for x in range(length - num):
                temp = temp.next

            print("{}th to last element --->".format(num), temp.data)

    def printList(self):
        n = self.head

        print('Printing Singly Linked List')
        while(n):
            print(n)
            n = n.next


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
        print('---Teardown successful---')

    def test1(self):
        self.link.printList()

    def test2(self):
        self.link.kthToLastElement(0)
        self.link.kthToLastElement(1)
        self.link.kthToLastElement(2)
        self.link.kthToLastElement(3)
        self.link.kthToLastElement(9)
        self.link.kthToLastElement(10)


if __name__ == "__main__":
    unittest.main()
