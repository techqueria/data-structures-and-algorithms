#!/usr/bin/python3
'''Queue via Stacks: Implement a MyQueue class
which implements a queue using two stacks.'''

import logging
import unittest


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.isEmpty():
            logging.debug('No stack to pop')
            return

        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.isEmpty():
            logging.debug('No stack to peek')
            return
        return self.stack[-1]

    def getStack(self):
        if self.isEmpty():
            logging.debug('No stack to peeek')
            return []

        return self.stack[::-1]

    def sort(self):
        r = Stack()
        while not self.isEmpty():
            temp = self.pop()
            logging.debug('Temp -> %r', temp)
            while not r.isEmpty() and r.peek() > temp:
                self.push(r.pop())
            r.push(temp)
            logging.debug('self stack %r', self.stack)
            logging.debug('%r', r.stack)

        while not r.isEmpty():
            self.push(r.pop())


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test1(self):
        arr = [2, 5, 7, 10, 3, 10, -1, -100]
        q = Stack()
        for x in arr:
            q.push(x)

        self.assertEqual(q.getStack(), [-100, -1, 10, 3, 10, 7, 5, 2])
        q.sort()
        self.assertEqual(q.getStack(), [-100, -1, 2, 3, 5, 7, 10, 10])


if __name__ == '__main__':
    unittest.main()
