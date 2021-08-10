"""
Python version 3.7.0
3.2 - Stack Min
How would you design a stack which, in addition to
push and pop, has a function min which returns the minimum element?
Push, pop and min should all operate in O(1) time.
"""

import copy
import unittest
import sys
from typing import List


class StackNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None # next is a pointer to a StackNode object
        self.running_min = sys.maxsize

class MyStack(object):
    """
    Stack data structure implementation.
    Uses LIFO (last-in first-out) ordering.
    The most recent item added to the stack is
    the first removed.  Traversal is top to bottom.
    """

    def __init__(self):
        self.top = None # top is a pointer to StackNode object
        self.size = 0
        self.min_value = sys.maxsize
        return
    
    def pop(self) -> int:
        """
        Removes the top item from the stack

        Raises:
            IndexError: raised when pop is attempted on empty stack

        Returns:
            int: The data at the top of the stack
        """
        if self.top is None:
            raise IndexError('Stack is Empty.')
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item
    
    def push(self, item: int) -> None:
        """
        Adds an item to the top of the stack
        Args:
            item (int): data we want at the top of stack
        """
        t = StackNode(item)
        t.next = self.top
        if self.top is None:
            t.running_min = item
            self.top = t
            self.size += 1
            print("Stack Node data = {}, local min = {}".format(item, t.running_min))
            return
        if item < self.top.data:
            t.running_min = item
        else:
            t.running_min = self.top.running_min
        print("Stack Node data = {}, local min = {}".format(item, t.running_min))
        self.top = t
        self.size += 1

    def min(self) -> int:
        """
        Returns the element with the lowest value in the stack

        Returns:
            int: min value in stack
        """
        return self.top.running_min

    def peek(self) -> int:
        """
        Returns data at the top of the stack

        Raises:
            IndexError: [description]

        Returns:
            int: the value at the top of the stack
        """
        if self.top is None:
            raise IndexError('Stack is Empty')
        return self.top.data
    
    def is_empty(self) -> bool:
        """
        Returns True if and only if the
        stack is empty, otherwise False.

        Returns:
            bool: True if empty, False otherwise
        """
        return self.size == 0
    
    def as_list(self) -> List[int]:
        """
        Builds a list of the current stack state.
        For example, given the following stack:
            3 -> 2 -> 1, where 3 is the top,
        Expect:
            [3, 2, 1]
        Returns:
            List[int]: list of integers
        """
        values = []
        n = self.top
        while n.next is not None:
            values.append(n.data)
            n = n.next
        values.append(n.data)
        return values
    
    def __str__(self):
        if self.size == 0:
            return '<Empty>'
        values = []
        n = self.top
        while n.next is not None:
            values.append(str(n.data))
            n = n.next
        values.append(str(n.data))
        return '->'.join(values)      


class TestMyStack(unittest.TestCase):
    def test_stack_push(self):
        s = MyStack()
        self.assertEqual(s.size, 0)
        self.assertEqual(s.top, None)
        s.push(2)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.top.data, 2)
        self.assertEqual(s.top.next, None)
        s.push(3)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.top.data, 3)
        self.assertEqual(s.top.next.data, 2)
        s.push(4)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.top.data, 4)
        self.assertEqual(s.top.next.data, 3)

        l = s.as_list()
        self.assertEqual(l, [4, 3, 2])
    
    def test_stack_peek(self):
        s = MyStack()
        with self.assertRaises(IndexError):
            s.peek()
        s.push(1)
        s.push(2)
        s.push(99)
        top_val = s.peek()
        self.assertEqual(top_val, 99)
    
    def test_stack_is_empty(self):
        s = MyStack()
        self.assertTrue(s.is_empty())
        s.push(7)
        self.assertFalse(s.is_empty())
    
    def test_stack_pop(self):
        # first case, attempt to pop an empty stack
        s = MyStack()
        with self.assertRaises(IndexError):
            s.pop()
        s.push(1)
        s.push(2)
        s.push(3)
        # size is 3
        self.assertEqual(s.as_list(), [3, 2, 1])
        val = s.pop()
        self.assertEqual(val, 3)
        self.assertEqual(s.size, 2) # size should now be 2
        self.assertEqual(s.as_list(), [2, 1])
    
    def test_stack_min(self):
        s = MyStack()
        s.push(9)
        self.assertEqual(s.min(), 9)
        s.push(7)
        self.assertEqual(s.min(), 7)
        s.push(-2)
        self.assertEqual(s.min(), -2)
        s.push(5)
        self.assertEqual(s.min(), -2)
        s.push(8)
        self.assertEqual(s.min(), -2)
        s.push(-99)
        self.assertEqual(s.min(), -99)
        s.push(2)
        self.assertEqual(s.min(), -99)
        s.pop()
        self.assertEqual(s.min(), -99)
        s.pop()
        self.assertEqual(s.min(), -2)
        s.pop()
        self.assertEqual(s.min(), -2)
        s.pop()
        self.assertEqual(s.min(), -2)
        s.pop()
        self.assertEqual(s.min(), 7)
        s.pop()
        self.assertEqual(s.min(), 9)
        s.pop()
        self.assertTrue(s.is_empty())


if __name__ == '__main__':
    unittest.main()
