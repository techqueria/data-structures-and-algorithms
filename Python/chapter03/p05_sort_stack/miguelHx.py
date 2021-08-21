"""3.5 - Sort Stack
Write a program to sort a stack such that the
smallest items are on the top. You can use an additional
temporary stack, but you may not copy the elements into
any other data structure (such as an array). The stack
supports the following operations
push, pop, peek, and isEmpty
"""

import copy
import unittest
import sys

from abc import abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar
from typing import List, Optional, Iterator

from typing import Protocol

T = TypeVar('T')

@dataclass
class StackNode(Generic[T]):
    data: T
    next: 'Optional[StackNode[T]]'

class MyStack(Generic[T]):
    """Stack data structure implementation.
    Uses LIFO (last-in first-out) ordering.
    The most recent item added to the stack is
    the first removed.  Traversal is top to bottom.
    """

    class MyStackIterator:
        def __init__(self, top: Optional[StackNode[T]], size: int):
            self.index = -1
            self.current_node = top
            self._size = size

        def __next__(self) -> T:
            self.index += 1
            if self.index == self._size or self.current_node is None:
                raise StopIteration
            n: T = self.current_node.data
            self.current_node = self.current_node.next
            return n

    def __init__(self):
        self.top: Optional[StackNode[T]] = None # top is a pointer to StackNode object
        self._size: int = 0

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
        self._size -= 1
        return item

    def push(self, item: T) -> None:
        """
        Adds an item to the top of the stack
        Args:
            item (T): data we want at the top of stack
        """
        t: StackNode = StackNode(item, None)
        t.next = self.top
        self.top = t
        self._size += 1

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

    def __iter__(self) -> MyStackIterator:
        """
        Builds a list of the current stack state.
        For example, given the following stack:
            3 -> 2 -> 1, where 3 is the top,
        Expect:
            [3, 2, 1]
        Returns:
            List[int]: list of integers
        """
        return self.MyStackIterator(self.top, self._size)

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

        # test adding different types, (float and int)
        s.push(1.2)
        self.assertEqual(len(s), 4)
        self.assertEqual(s.top.data, 1.2)
        self.assertEqual(s.top.next.data, 4)
        self.assertEqual(list(s), [1.2, 4, 3, 2])

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

    def test__bool__(self):
        s = MyStack()
        self.assertFalse(s)
        s.push(3)
        self.assertTrue(s)


def sorted_stack(stack: MyStack) -> MyStack:
    """This function will take in a stack
    and return a sorted copy.
    In order to do this, we need to find the biggest
    number in an input stack copy, and then push it to the
    output stack. Repeat until input stack copy is empty.

    Args:
        stack (MyStack): stack of items

    Returns:
        MyStack: sorted stack of items, with smallest items on top
    """
    # make copy of stack argument.
    temp_stack = MyStack()

if __name__ == '__main__':
    unittest.main()
