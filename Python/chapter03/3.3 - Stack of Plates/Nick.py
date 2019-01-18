#!/usr/bin/python3

import unittest
from random import randint


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
            print('No value to add to stack')
            return
        s = Stack()
        s.push(value)
        self.stack.append(s)

    def popLastStack(self):
        if self.length() == 0:
            print('No set of stacks to pop')
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

    def printAllStacks(self):
        print('pointer', self.pointer)
        print('length', self.length())
        for x in range(len(self.stack)):
            print('Set number {} and values -> {}'.format(x,
                                                          self.stack[x].stack))


class Stack:
    def __init__(self):
        self.stack = []
        self.min = None

    def getMin(self):
        return self.min

    def pop(self):
        if not self.length:
            print('No stack to pop')
            return

        item = self.stack.pop()
        print('Item popped', item)

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
        print('Item added to stack', value)

    def peek(self):
        if not self.length:
            print('No stack to peek')
            return
        print('Peeking into stack', self.stack[-1])

    def printStack(self):
        if not self.length:
            print('No stack to peeek')
            return

        print("Top of stack\n _ ")
        for x in self.stack[::-1]:
            print('|', x, '|')
            print('|', '_', '|')


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def generateRand(self, size=15):
        return [randint(0, 100) for x in range(size)]

    def test1(self):
        arr = self.generateRand()
        setStack1 = SetofStacks()
        for x in arr:
            setStack1.push(x)
        setStack1.printAllStacks()

        for x in range(randint(7, len(arr))):
            setStack1.popLastStack()
        setStack1.printAllStacks()


if __name__ == '__main__':
    unittest.main()
