"""
Python version 3.7.0
3.3 - Stack of Plates
Imagine a (literal) stack of plates.  If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack
exceeds some threshold. Implement a data structure SetOfStacks that mimics this.
SetOfStacks should be composed of several stacks and should create a new stack once
the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
behave identically to a single stack (that is, pop() should return the same values as it would
if there were just a single stack).

FOLLOW UP:
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
"""

import copy
import unittest
from typing import List


class StackNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None # next is a pointer to a StackNode object

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
        self.top = t
        self.size += 1

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


if __name__ == '__main__':
    unittest.main()