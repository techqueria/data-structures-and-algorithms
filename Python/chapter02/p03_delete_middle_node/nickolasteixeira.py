#!/usr/bin/python3
import unittest
from random import randint
'''
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node. EXAMPLE lnput:the node c from the linked lista->b->c->d->e->f Result: nothing is returned, but the new linked list looks like a->b->d->e->f Hints:#72
'''

'''
Get clarification on this question:
1. Will I always know that I will get a middle node? (non end or head node)
2. What if the node is only 2 lengths long?
3. What input will I get?
'''


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
        # adds node to head if no head
        node = Node(data)
        if not self.head:
            self.head = node
        # adds to end of linked list
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def toList(self):
        if self.head is None:
            return []

        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

    def findSize(self):
        if self.head is None:
            print('Nothing to find the size of')
            return

        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def findMiddleNode(self):
        size = self.findSize()
        if size and size > 2:
            # cannot be the size of the node (tail) or the first node (head)
            temp = self.head
            randomNum = randint(2, size - 1)
            for x in range(1, randomNum):
                temp = temp.next
            return temp
        else:
            print("Not able to access a non head or tail node")
            return None

    def deleteMiddleNode(self, node):
        '''The solution is simply to copy the data
        from the next node over to the current node,
        and then to delete the next node.
        '''
        if node is None:
            print('No node to delete')
            return

        temp = node.next
        node.data = temp.data
        node.next = temp.next
        del temp


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.l = SinglyLinkedList()
        cls.l.addNode(-1)
        cls.l.addNode(3)
        cls.l.addNode('hello')
        cls.l.addNode(100)
        cls.l.addNode(5)

    @classmethod
    def tearDownClass(self):
        pass

    def test1(self):
        numNodes = self.l.findSize()
        self.assertEqual(numNodes, 5)

    def test2(self):
        node = self.l.findMiddleNode()
        self.assertIn(node.data, [100, 'hello', 3])
        self.l.deleteMiddleNode(node)
        self.assertIn(self.l.toList(), [
            [-1, 3, 100, 5],
            [-1, 3, 'hello', 5],
            [-1, 'hello', 100, 5],
        ])


if __name__ == '__main__':
    unittest.main()
