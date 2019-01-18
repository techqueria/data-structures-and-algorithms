#!/usr/bin/python3
'''Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting'''
import unittest


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def appendNode(self, data, next=None):
        node = Node(data, next)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        print('Node added to LL-->', data)

    def printMemoryValues(self):
        temp = self.head
        while temp:
            print('Memory address values: ', hex(
                id(temp)), ' Values: ', temp.data)
            temp = temp.next

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

    def findLongest(self, l1, l2):
        if not self.head:
            print('No list to iterate')
            return None

        l1count, l2count = 0, 0
        temp1, temp2 = l1.head, l2.head
        while temp1:
            l1count += 1
            temp1 = temp1.next

        while temp2:
            l2count += 1
            temp2 = temp2.next

        if l1count > l2count:
            longest, shortest = l1, l2
        else:
            longest, shortest = l2, l1
        return abs(l1count - l2count), longest, shortest

    def intersection(self, l1, l2):
        if not l1.head or not l2.head:
            print('No list to iterate -> intersection')
            return None

        diff, longest, shortest = self.findLongest(l1, l2)
        temp = longest.head
        for x in range(diff):
            temp = temp.next

        temp2 = shortest.head
        while temp:
            if temp == temp2:
                return temp
            temp = temp.next
            temp2 = temp2.next

        return None


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.l = SinglyLinkedList()
        cls.l.appendNode(3)
        cls.l.appendNode(1)
        cls.l.appendNode(5)
        cls.l.appendNode(9)
        cls.l.appendNode(7)
        cls.l.appendNode(2)
        cls.l.appendNode(1)
        cls.l.printMemoryValues()

        cls.k = SinglyLinkedList()
        cls.k.appendNode(4)
        node = cls.l.findNode(7)
        cls.k.appendNode(6, node)
        cls.k.printMemoryValues()

        cls.p = SinglyLinkedList()
        cls.p.appendNode(1)
        cls.p.appendNode(2)
        cls.p.appendNode(5)
        cls.p.appendNode(1000)
        cls.p.appendNode(-22)
        cls.p.printMemoryValues()

    @classmethod
    def tearDownClass(cls):
        pass

    def printStatement(self, interNode):
        if interNode:
            print('Nodes intersect at address', hex(
                id(interNode)), ' Value: ', interNode.data)
        else:
            print('Nodes do not intersect')

    def test1(self):
        interNode = self.l.intersection(self.l, self.k)
        interNode2 = self.l.intersection(self.l, self.p)
        self.printStatement(interNode)
        self.printStatement(interNode2)


if __name__ == '__main__':
    unittest.main()
