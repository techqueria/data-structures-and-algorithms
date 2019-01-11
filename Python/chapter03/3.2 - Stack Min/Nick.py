#!/usr/bin/python3

import unittest


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

    def test1(self):
        arr = [2, 5, 7, 10, 3, 10, -1]
        s = Stack()
        for x in arr:
            s.push(x)
        s.printStack()
        print('Min value in stack -->', s.getMin())
        s.pop()
        print('Min value after pop -->', s.getMin())


if __name__ == '__main__':
    unittest.main()
