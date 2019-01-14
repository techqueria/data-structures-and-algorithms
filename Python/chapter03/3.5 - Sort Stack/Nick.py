#!/usr/bin/python3
'''Queue via Stacks: Implement a MyQueue class
which implements a queue using two stacks.'''
import unittest


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.isEmpty():
            print('No stack to pop')
            return

        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.isEmpty():
            print('No stack to peek')
            return
        return self.stack[-1]

    def printStack(self):
        if self.isEmpty():
            print('No stack to peeek')
            return

        print("Top of stack\n _ ")
        for x in self.stack[::-1]:
            print('|', x, '|')
            print('|', '_', '|')

    def sort(self):
        r = Stack()
        while not self.isEmpty():
            temp = self.pop()
            print('Temp ->', temp)
            while not r.isEmpty() and r.peek() > temp:
                self.push(r.pop())
            r.push(temp)
            print('self stack', self.stack)
            print(r.stack, end='\n\n')

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
        print(arr)
        q = Stack()
        for x in arr:
            q.push(x)

        q.printStack()
        q.sort()
        q.printStack()


if __name__ == '__main__':
    unittest.main()
