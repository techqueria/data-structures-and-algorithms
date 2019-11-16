#!/usr/bin/python3

import logging
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
        logging.debug("Node added --> %r", data)

    def findLength(self, ll):
        if not ll.head:
            logging.debug('No list to traverse')
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
            logging.debug('No list to traverse')
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
        logging.debug("Number to sum: %r", num)
        return num

    def addTwoLinkedLists(self, l1, l2, direction=True):
        num1 = self.turnIntoNum(l1, direction)
        num2 = self.turnIntoNum(l2, direction)
        if num1 and num2:
            return num1 + num2
        else:
            logging.debug('No numbers to return')
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
        self.assertEqual(sumReverse, 912)
        sumLL = self.l.addTwoLinkedLists(self.l, self.k)
        self.assertEqual(sumLL, 1308)


if __name__ == '__main__':
    unittest.main()
