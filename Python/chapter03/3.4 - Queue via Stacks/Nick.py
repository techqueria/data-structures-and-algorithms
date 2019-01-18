#!/usr/bin/python3
'''Queue via Stacks: Implement a MyQueue class
which implements a queue using two stacks.'''
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

    def peek(self):
        if not self.length:
            print('No stack to peek')
            return
        return self.stack[-1]

    def printStack(self):
        if not self.length:
            print('No stack to peeek')
            return

        print("Top of stack\n _ ")
        for x in self.stack[::-1]:
            print('|', x, '|')
            print('|', '_', '|')


class MyQueue:
    def __init__(self):
        self.newStack = Stack()
        self.oldStack = Stack()

    def push(self, value):
        self.newStack.push(value)

    def pop(self):
        self.rotate()
        if self.oldStack.length() == 0:
            print('Nothing to pop in this queue')
            return
        return self.oldStack.pop()

    def peek(self):
        self.rotate()
        if self.oldStack.length() == 0:
            print('Nothing to peek in this queue')
            return
        return self.oldStack.peek()

    def rotate(self):
        if (self.oldStack.length() == 0):
            while not self.newStack.length() == 0:
                self.oldStack.push(self.newStack.pop())

    def printQueue(self):
        self.rotate()
        for x in self.oldStack.stack[::-1]:
            print('Item in Queue -->', x)

        for x in self.newStack.stack:
            print('Item in Queue -->', x)


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test1(self):
        arr = [2, 5, 7, 10, 3, 10, -1, -100]
        print(arr)
        q = MyQueue()
        for x in arr:
            q.push(x)

        q.printQueue()
        print('First in Queue --> Popped', q.pop())
        print('Second in Queue --> Popped', q.pop())
        q.printQueue()
        print('Let\'s take a peek -->', q.peek())


if __name__ == '__main__':
    unittest.main()
