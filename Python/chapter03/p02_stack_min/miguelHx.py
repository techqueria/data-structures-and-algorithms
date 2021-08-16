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

from abc import abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar
from typing import List, Optional, Iterator

T = TypeVar('T')
C = TypeVar('C', bound='Comparable')

class Comparable(Generic[T, C]):
    @abstractmethod
    def __lt__(self, other: T):
        pass

@dataclass
class StackNode(Generic[T, C]):
    data: T
    next: 'Optional[StackNode[T, C]]'
    running_min: T

class MyStack(object):
    """Stack data structure implementation.
    Uses LIFO (last-in first-out) ordering.
    The most recent item added to the stack is
    the first removed.  Traversal is top to bottom.
    """

    def __init__(self):
        self.top: Optional[StackNode[T]] = None # top is a pointer to StackNode object
        self._size: int = 0
        self.index: int = -1 # for iterator use
        self.current_node: Optional[StackNode[T]] = self.top # also for iterator use
        return
    
    def pop(self) -> T:
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
        self.current_node = self.top
        self._size -= 1
        return item
    
    def push(self, item: T) -> None:
        """
        Adds an item to the top of the stack
        Args:
            item (T): data we want at the top of stack
        """
        t: StackNode = StackNode(item, None, sys.maxsize)
        t.next = self.top
        if self.top is None:
            t.running_min = item
        elif item < self.top.data: # we will assume data implements __lt__
            t.running_min = item
        else:
            t.running_min = self.top.running_min
        # print("Stack Node data = {}, local min = {}".format(item, t.running_min))
        self.top = t
        self.current_node = self.top
        self._size += 1

    def min(self) -> T:
        """
        Returns the element with the lowest value in the stack

        Returns:
            int: min value in stack
        """
        if self.top is None:
            raise ValueError('Min does not exist yet because there are no values in the stack.')
        return self.top.running_min

    def peek(self) -> T:
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
    
    def __iter__(self) -> Iterator:
        """
        Builds a list of the current stack state.
        For example, given the following stack:
            3 -> 2 -> 1, where 3 is the top,
        Expect:
            [3, 2, 1]
        Returns:
            List[int]: list of integers
        """
        return self
    
    def __next__(self) -> T:
        self.index += 1
        if self.index == self._size or self.current_node is None:
            self.index = -1
            self.current_node = self.top
            raise StopIteration
        n: T = self.current_node.data
        self.current_node = self.current_node.next
        return n
    
    def __bool__(self) -> bool:
        """
        True is returned when the container is not empty.
        From https://docs.python.org/3/reference/datamodel.html#object.__bool__ :
        Called to implement truth value testing and the built-in operation bool();
        should return False or True. When this method is not defined, len() is called,
        if it is defined, and the object is considered true if its result is nonzero.
        If a class defines neither len() nor bool(), all its instances are considered true.
        Returns:
            bool: False when empty, True otherwise
        """
        return self._size > 0
    
    def __len__(self) -> int:
        return self._size
    
    def __str__(self):
        if self._size == 0:
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
        self.assertEqual(len(s), 0)
        self.assertEqual(s.top, None)
        s.push(2)
        self.assertEqual(len(s), 1)
        self.assertEqual(s.top.data, 2)
        self.assertEqual(s.top.next, None)
        s.push(3)
        self.assertEqual(len(s), 2)
        self.assertEqual(s.top.data, 3)
        self.assertEqual(s.top.next.data, 2)
        s.push(4)
        self.assertEqual(len(s), 3)
        self.assertEqual(s.top.data, 4)
        self.assertEqual(s.top.next.data, 3)
        self.assertEqual(list(s), [4, 3, 2])
    
    def test_stack_peek(self):
        s = MyStack()
        with self.assertRaises(IndexError):
            s.peek()
        s.push(1)
        s.push(2)
        s.push(99)
        top_val = s.peek()
        self.assertEqual(top_val, 99)
    
    def test_stack_pop(self):
        # first case, attempt to pop an empty stack
        s = MyStack()
        with self.assertRaises(IndexError):
            s.pop()
        s.push(1)
        s.push(2)
        s.push(3)
        # size is 3
        self.assertEqual(list(s), [3, 2, 1])
        val = s.pop()
        self.assertEqual(val, 3)
        self.assertEqual(s._size, 2) # size should now be 2
        self.assertEqual(list(s), [2, 1])
    
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
        self.assertTrue(not s)
    
    def test__bool__(self):
        s = MyStack()
        self.assertFalse(s)
        s.push(3)
        self.assertTrue(s)


if __name__ == '__main__':
    unittest.main()
