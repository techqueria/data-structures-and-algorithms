"""Python version 3.7.0
3.4 - Queue via Stacks:
Implement a MyQueue class which implements a queue using two stacks.
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


class MyStack(Generic[T]):
    """Stack data structure implementation.
    Uses LIFO (last-in first-out) ordering.
    The most recent item added to the stack is
    the first removed.  Traversal is top to bottom.
    """
    def __init__(self):
        self.top: Optional[StackNode[T]] = None # top is a pointer to StackNode object
        self._size: int = 0
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
        self._size -= 1
        return item

    def push(self, item: T) -> None:
        """
        Adds an item to the top of the stack
        Args:
            item (int): data we want at the top of stack
        """
        t = StackNode(item, None)
        t.next = self.top
        self.top = t
        self.current_node = self.top
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
    
    def empty(self) -> None:
        while self._size > 0:
            self.pop()

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


@dataclass
class QueueNode(Generic[T]):
    data: T
    next: 'Optional[QueueNode[T]]'


class MyQueue(Generic[T]):
    def __init__(self):
        self._size = 0
        self.data_stack = MyStack[T]()  # will be used as main data container
    
    def add(self, item: T):
        self.data_stack.push(item)
        self._size += 1
    
    def _produce_reversed_stack(self, input_stack: MyStack) -> MyStack:
        """This function will take in a stack,
        and return a copy of a reversed version of that
        stack.

        Args:
            input_stack (MyStack): Stack of type T
        """
        temp_stack = MyStack[T]()
        while len(input_stack) > 0:
            d = input_stack.pop()
            temp_stack.push(d)
        return temp_stack

    def _pop(self) -> T:
        # 1. local temp stack
        temp_stack: MyStack = self._produce_reversed_stack(self.data_stack)
        # 2. extract value at top of 2nd stack.
        data: T = temp_stack.pop()
        # 3. move remaining values back to stack one
        self.data_stack = self._produce_reversed_stack(temp_stack)
        return data

    def remove(self) -> T:
        if self._size == 0:
            raise Exception('No values in stack to remove')
        # use second stack to extract item of interest
        data: T = self._pop()
        self._size -= 1
        return data

    def _peek(self) -> T:
        # 1. local temp stack
        temp_stack: MyStack = self._produce_reversed_stack(self.data_stack)
        # 2. extract value at top of 2nd stack.
        data: T = temp_stack.peek()
        # 3. move remaining values back to stack one
        self.data_stack = self._produce_reversed_stack(temp_stack)
        return data

    def peek(self) -> T:
        if self._size == 0:
            raise Exception('No values in stack to remove')
        return self._peek()

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

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


class TestMyQueue(unittest.TestCase):
    def test_add(self):
        q = MyQueue()
        self.assertEqual(len(q), 0)
        # going to add 1, 3, 5.
        # FIFO, so when removing, 1 goes out first
        q.add(1)
        self.assertEqual(len(q), 1)
        self.assertEqual(q.peek(), 1)
        q.add(3)
        self.assertEqual(len(q), 2)
        self.assertEqual(q.peek(), 1)
        q.add(5)
        self.assertEqual(len(q), 3)
        self.assertEqual(q.peek(), 1)
    
    def test_remove(self):
        q = MyQueue()
        q.add(1)
        q.add(2)
        q.add(3)
        val = q.remove()
        self.assertEqual(val, 1)
        val = q.remove()
        self.assertEqual(val, 2)
        val = q.remove()
        self.assertEqual(val, 3)
        self.assertRaises(Exception, lambda: q.remove())

    def test_peek(self):
        q = MyQueue()
        self.assertRaises(Exception, lambda: q.peek())
        q.add(99)
        q.add(45)
        self.assertEqual(q.peek(), 99)
    
    def test_is_empty(self):
        q = MyQueue()
        self.assertTrue(q.is_empty())
        self.assertFalse(q)
        q.add(100)
        self.assertFalse(q.is_empty())
        self.assertTrue(q)


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
        self.assertEqual(len(s), 2) # size should now be 2
        self.assertEqual(list(s), [2, 1])

    def test__bool__(self):
        s = MyStack()
        self.assertFalse(s)
        s.push(3)
        self.assertTrue(s)


if __name__ == '__main__':
    unittest.main()