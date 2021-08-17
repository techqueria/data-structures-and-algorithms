"""Python version 3.7.0
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

from dataclasses import dataclass
from typing import Generic, TypeVar
from typing import List, Optional, Iterator

T = TypeVar('T')

@dataclass
class StackNode(Generic[T]):
    data: T
    next: 'Optional[StackNode[T]]'


class MyStack:
    """Stack data structure implementation.
    Uses LIFO (last-in first-out) ordering.
    The most recent item added to the stack is
    the first removed.  Traversal is top to bottom.
    """

    def __init__(self):
        self.top: Optional[StackNode[T]] = None # top is a pointer to StackNode object
        self.size: int = 0
        self.index: int = -1 # tracking current node for iterator use
        self.current_node: Optional[StackNode[T]] = self.top
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
        self.size -= 1
        return item

    def push(self, item: int) -> None:
        """
        Adds an item to the top of the stack
        Args:
            item (int): data we want at the top of stack
        """
        t = StackNode(item, None)
        t.next = self.top
        self.top = t
        self.current_node = self.top
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
        if self.index == self.size or self.current_node is None:
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
        return self.size > 0

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
        l = list(s)
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
        self.assertEqual(s.size, 2) # size should now be 2
        self.assertEqual(list(s), [2, 1])

    def test__bool__(self):
        s = MyStack()
        self.assertFalse(s)
        s.push(3)
        self.assertTrue(s)



if __name__ == '__main__':
    unittest.main()