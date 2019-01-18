#!/usr/bin/python3

import unittest


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        print("Node added -->", data)

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def findLength(self, ll):
        if not ll.head:
            print('No list to traverse')
            return
        temp = ll.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def turnIntoNum(self, ll, direction=True):
        '''if direction = true, then sum in place
            if direction = false, then reverse the ll to sum'''

        if not ll.head:
            print('No list to traverse')
            return
        num = 0
        length = self.findLength(ll)
        if direction:
            power = length - 1
        n = 0
        temp = ll.head
        while n < length:
            if direction:
                num += temp.data * (10 ** power)
                power -= 1
            else:
                num += temp.data * (10 ** n)
            temp = temp.next
            n += 1
        print("Number to sum", num)
        return num

    def addTwoLinkedLists(self, l1, l2, direction=True):
        num1 = self.turnIntoNum(l1, direction)
        num2 = self.turnIntoNum(l2, direction)
        if num1 and num2:
            return num1 + num2
        else:
            print('No numbers to return')
            return


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.l = SinglyLinkedList()
        cls.l.addNode(7)
        cls.l.addNode(1)
        cls.l.addNode(6)

        cls.k = SinglyLinkedList()
        cls.k.addNode(5)
        cls.k.addNode(9)
        cls.k.addNode(2)

    @classmethod
    def tearDownClass(cls):
        pass

    def test1(self):
        sumReverse = self.l.addTwoLinkedLists(self.l, self.k, False)
        print('Sum ->', sumReverse)
        sumLL = self.l.addTwoLinkedLists(self.l, self.k)
        print('Sum ->', sumLL)


if __name__ == '__main__':
    unittest.main()
