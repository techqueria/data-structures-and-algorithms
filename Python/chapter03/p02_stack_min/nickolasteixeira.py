#!/usr/bin/python3

import logging
import unittest


class Stack:
    def __init__(self):
        self.stack = []
        self.min = None

    def getMin(self):
        return self.min

    def pop(self):
        if not self.length:
            logging.debug('No stack to pop')
            return None

        item = self.stack.pop()
        logging.debug('Item popped %r', item)

        if item == self.min:
            if self.length() > 0:
                self.findMin()
            else:
                self.min = None
        return item

    def findMin(self):
        self.min = self.stack[0]
        for x in self.stack:
            if x < self.min:
                self.min = x

    def length(self):
        return len(self.stack)

    def push(self, value):
        if not self.min:
            self.min = value
        elif value < self.min:
            self.min = value

        self.stack.append(value)
        logging.debug('Item added to stack %r', value)

    def peek(self):
        if not self.length:
            logging.debug('No stack to peek')
            return
        logging.debug('Peeking into stack %r', self.stack[-1])


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test1(self):
        arr = [2, 5, 7, 10, 3, 10, -1]
        s = Stack()
        for x in arr:
            s.push(x)
        self.assertEqual(s.getMin(), -1)
        self.assertEqual(s.pop(), -1)
        self.assertEqual(s.getMin(), 2)


if __name__ == '__main__':
    unittest.main()
