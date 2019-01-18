#!/usr/bin/python3
import unittest


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data, next=None):
        node = Node(data, next)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        print('Node added to LL-->', data)

    def findNode(self, value):
        if not self.head:
            print('No list to iterate')
            return

        temp = self.head
        while temp:
            if temp.data == value:
                return temp
            temp = temp.next
        return None

    def printList(self):
        temp = self.head
        while temp:
            print('->', temp.data)
            temp = temp.next

    def loopDetection(self):
        if not self.head:
            print('No list to iterate for loop detection')
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        slow = self.head
        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return fast


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.l = SinglyLinkedList()
        cls.l.addNode(3)
        cls.l.addNode(1)
        cls.l.addNode(5)
        cls.l.addNode(9)
        cls.l.addNode(7)
        cls.l.addNode(2)
        cls.l.addNode(10)
        cls.l.printList()

        cls.k = SinglyLinkedList()
        cls.k.addNode(1)
        cls.k.addNode(10)
        cls.k.addNode(15)
        cls.k.addNode(16)
        cls.k.addNode(1)
        cls.k.printList()

    @classmethod
    def tearDownClass(cls):
        pass

    def printStatement(self, node):
        if node:
            print("Start of Loop", hex(id(node)), '-->', node.data)
        else:
            print('No loop detected')

    def test1(self):
        node = self.l.findNode(10)
        node.next = self.l.findNode(5)
        # if uncomment below, will print in infinite
        # self.l.printList()
        start = self.l.loopDetection()
        self.printStatement(start)

    def test2(self):
        start = self.k.loopDetection()
        self.printStatement(start)


if __name__ == '__main__':
    unittest.main()
