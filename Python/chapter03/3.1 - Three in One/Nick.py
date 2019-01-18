#!/usr/bin/python3

import unittest


def breakIntoThrees(arr):
    if len(arr) <= 2:
        print('Cannot break into 3 pieces')
        return

    print('Breaking array into three pieces', arr)
    breakpoint = len(arr) // 3
    s1, s2, s3 = Stack(), Stack(), Stack()
    inputIntoThrees(s1, arr[:breakpoint])
    inputIntoThrees(s2, arr[breakpoint:breakpoint * 2])
    inputIntoThrees(s3, arr[breakpoint * 2:])
    return s1, s2, s3


def inputIntoThrees(dastack, arr):
    print('Creating a new stack')
    for x in arr:
        dastack.push(x)
    print()


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if not self.length:
            print('No stack to pop')
            return

        item = self.stack.pop()
        print('Item popped', item)
        return item

    def length(self):
        return len(self.stack)

    def push(self, value):
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
        arr = [2, 5, 7, 10, 3, -1]
        s1, s2, s3 = breakIntoThrees(arr)
        s1.printStack()
        s2.printStack()
        s3.printStack()

        arr1 = [2, 1, 4, 4, 6, 6, 6]
        s3, s4, s5 = breakIntoThrees(arr1)
        s5.printStack()

if __name__ == '__main__':
    unittest.main()
