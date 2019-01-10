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
            self.head = n
        else:
            n = self.head
            while (n.next):
                n = n.next

            print('New Node added ---->', data)
            new_node = Node(data)
            n.next = new_node

    def removeDuplicates(self):
        print('Removing Duplicates.')
        temp = self.head
        nums = set()
        while temp.next:
            nums.add(temp.data)
            if temp.next.data in nums:
                temp.next = temp.next.next
            temp = temp.next
        print('Duplicates Removed!---------')

    def removeDuplicatesNoBuffer(self):
        print('Removing Duplicates - No buffer')
        temp = self.head
        while temp.next:
            second = temp
            while second.next:
                if second.data == second.next.data:
                    second.next = second.next.next
                second = second.next
            temp = temp.next
        print('Duplicates Removed!----------')

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
        self.link.removeDuplicates()
        self.link.printList()

    def test3(self):
        self.link.addNode(-1)
        self.link.addNode(20)
        self.link.addNode(40)
        self.link.printList()
        self.link.removeDuplicatesNoBuffer()
        self.link.printList()

    def test4(self):
        self.link.insertHead(-2)
        self.link.printList()


if __name__ == "__main__":
    unittest.main()
