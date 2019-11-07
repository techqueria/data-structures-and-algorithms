#!/usr/bin/python3

import logging
import unittest


class SetofStacks:
    def __init__(self, limit=5):
        self.stack = []
        self.pointer = None
        self.limit = limit

    def length(self):
        if self.pointer is None:
            return 0
        else:
            tlength = self.pointer * self.limit
            s = self.stack[self.pointer]
            for x in s.stack:
                tlength += 1
            return tlength

    def push(self, value):
        if self.pointer is None:
            # set pointer, add to stack
            self.addNewStack(value)
            self.pointer = 0
        else:
            # check for limit before creating
            # or adding a new stack
            s = self.stack[self.pointer]
            if s.length() == self.limit:
                self.addNewStack(value)
                self.pointer += 1
            else:
                s.push(value)

    def addNewStack(self, value):
        if not value:
            logging.debug('No value to add to stack')
            return
        s = Stack()
        s.push(value)
        self.stack.append(s)

    def popLastStack(self):
        if self.length() == 0:
            logging.debug('No set of stacks to pop')
            return
        s = self.stack[self.pointer]
        s.pop()
        if self.length() == 0:
            if s.length() == 0:
                self.pointer = 0
        else:
            if s.length() == 0:
                del self.stack[self.pointer]
                self.pointer -= 1

    def getAllStacks(self):
        return [stack.stack for stack in self.stack]


class Stack:
    def __init__(self):
        self.stack = []
        self.min = None

    def getMin(self):
        return self.min

    def pop(self):
        if not self.length:
            logging.debug('No stack to pop')
            return

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

    def printStack(self):
        if not self.length:
            logging.debug('No stack to peeek')
            return

        logging.debug("Top of stack\n _ ")
        for x in self.stack[::-1]:
            logging.debug('|%r|', x)
            logging.debug('|_|')


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test1(self):
        arr = [100, 80, 70, 65, 33, 35, 31, 45, 48, 35, 33, 94, 72, 65, 9]
        setStack1 = SetofStacks()
        for x in arr:
            setStack1.push(x)
        self.assertEqual(setStack1.getAllStacks(), [
            [100, 80, 70, 65, 33],
            [35, 31, 45, 48, 35],
            [33, 94, 72, 65, 9],
        ])
        for _ in range(14):
            setStack1.popLastStack()
        self.assertEqual(setStack1.getAllStacks(), [
            [100],
        ])


if __name__ == '__main__':
    unittest.main()
