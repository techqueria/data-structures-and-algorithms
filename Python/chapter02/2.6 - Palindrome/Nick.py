#!/usr/bin/python3

import unittest


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def appendNode(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        print('Node added to LL-->', data)

    def isPalindrome(self):
        if not self.head:
            print('No LL to traverse')
            return

        pali = []
        temp = self.head
        while temp:
            pali.append(temp.data)
            temp = temp.next

        strpali = ''.join(pali)
        return strpali == strpali[::-1]


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.l = SinglyLinkedList()
        cls.l.appendNode('r')
        cls.l.appendNode('a')
        cls.l.appendNode('c')
        cls.l.appendNode('e')
        cls.l.appendNode('c')
        cls.l.appendNode('a')
        cls.l.appendNode('r')

        cls.k = SinglyLinkedList()
        cls.k.appendNode('n')
        cls.k.appendNode('i')
        cls.k.appendNode('c')
        cls.k.appendNode('k')

    @classmethod
    def tearDownClass(cls):
        pass

    def test1(self):
        self.assertTrue(self.l.isPalindrome())
        self.assertFalse(self.k.isPalindrome())


if __name__ == '__main__':
    unittest.main()
