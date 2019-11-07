#!/usr/bin/python3

import logging
import unittest


def breakIntoThrees(arr):
    if len(arr) <= 2:
        logging.debug('Cannot break into 3 pieces')
        return

    logging.debug('Breaking array into three pieces %r', arr)
    breakpoint = len(arr) // 3
    s1, s2, s3 = Stack(), Stack(), Stack()
    inputIntoThrees(s1, arr[:breakpoint])
    inputIntoThrees(s2, arr[breakpoint:breakpoint * 2])
    inputIntoThrees(s3, arr[breakpoint * 2:])
    return s1, s2, s3


def inputIntoThrees(dastack, arr):
    logging.debug('Creating a new stack')
    for x in arr:
        dastack.push(x)
    logging.debug('')


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if not self.length:
            logging.debug('No stack to pop')
            return

        item = self.stack.pop()
        logging.debug('Item popped', item)
        return item

    def length(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)
        logging.debug('Item added to stack', value)

    def peek(self):
        if not self.length:
            logging.debug('No stack to peek')
            return
        logging.debug('Peeking into stack', self.stack[-1])

    def toList(self):
        if not self.length:
            logging.debug('No stack to peeek')
            return []

        return self.stack[::-1]


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test1(self):
        arr = [2, 5, 7, 10, 3, -1]
        s1, s2, s3 = breakIntoThrees(arr)
        self.assertEqual(s1.toList(), [5, 2])
        self.assertEqual(s2.toList(), [10, 7])
        self.assertEqual(s3.toList(), [-1, 3])

        arr1 = [2, 1, 4, 4, 6, 6, 6]
        s3, s4, s5 = breakIntoThrees(arr1)
        self.assertEqual(s5.toList(), [6, 6, 6])

if __name__ == '__main__':
    unittest.main()
