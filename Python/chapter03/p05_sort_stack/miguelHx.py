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

T = TypeVar('T', bound='Comparable')

class Comparable(Protocol):
    @abstractmethod
    def __gt__(self, other: T) -> bool:
        pass

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

    class MyStackIterator(Iterator[T]):
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

    def __init__(self, *numbers: T):
        self.top: Optional[StackNode[T]] = None # top is a pointer to StackNode object
        self._size: int = 0
        for num in numbers:
            self.push(num)

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
        t: StackNode[T] = StackNode(item, None)
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

    def __iter__(self) -> MyStackIterator[T]:
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

    def __str__(self) -> str:
        if self._size == 0:
            return '<Empty>'
        values = []
        n = self.top
        while n and n.next:
            values.append(str(n.data))
            n = n.next
        if n:
            values.append(str(n.data))
        return '->'.join(values)


class TestMyStack(unittest.TestCase, Generic[T]):
    def test_stack_push(self) -> None:
        s: MyStack[T] = MyStack()
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

    def test_stack_peek(self) -> None:
        s: MyStack[T] = MyStack()
        with self.assertRaises(IndexError):
            s.peek()
        s.push(1)
        s.push(2)
        s.push(99)
        top_val = s.peek()
        self.assertEqual(top_val, 99)

    def test_stack_pop(self) -> None:
        # first case, attempt to pop an empty stack
        s: MyStack[T] = MyStack()
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

    def test__bool__(self) -> None:
        s: MyStack[T] = MyStack()
        self.assertFalse(s)
        s.push(3)
        self.assertTrue(s)


def sorted_stack(stack: MyStack[T]) -> None:
    """This function will take in a stack
    and modify the input stack to be sorted such 
    that the smallest elements are at the top.
    Runtime: O(n^2)
    Space: O(n) where n is the number of elements in the input stack.

    Args:
        stack (MyStack): stack of items
    """
    # create temporary auxiliary stack
    num_ops = 0
    aux_stack: MyStack[T] = MyStack()
    while stack:
        t: T = stack.pop()
        num_ops += 1
        while aux_stack and aux_stack.peek() > t:
            num_ops += 1
            stack.push(aux_stack.pop())
        aux_stack.push(t)
    # elements are in order with highest values
    # on top. Need to put elements back into original stack.
    print("num core operations (operations dependent on size of stack) when n is {}: {}".format(len(aux_stack), num_ops))
    while aux_stack:
        stack.push(aux_stack.pop())


class TestSortStack(unittest.TestCase, Generic[T]):
    def test_sort_stack_average_case(self) -> None:
        s: MyStack[T] = MyStack(1, 9, 5, 7, 3, 8)
        # will look like this (leftmost is top of stack):
        # [8, 3, 7, 5, 9, 1]
        self.assertEqual(list(s), [8, 3, 7, 5, 9, 1])
        # after sorting, should look like this (smallest values on top):
        # [1, 3, 5, 7, 8, 9]
        print("Sorting stack average case")
        sorted_stack(s)
        self.assertEqual(list(s), [1, 3, 5, 7, 8, 9])

    def test_sort_stack_ascending_order_worst_case(self):
        # ascending order runtime is worst case with a complexity
        # of O(n^2).
        # Why? Because for every element e in stack of size n,
        # we will need to shift more elements as we get closer
        # to sorting completion and the number of operations
        # increases parabolically.
        s: MyStack[T] = MyStack(1, 2, 3, 4, 5)
        # will look like this (leftmost is top of stack):
        # [5, 4, 3, 2, 1]
        self.assertEqual(list(s), [5, 4, 3, 2, 1])
        # after sorting, should look like this (smallest values on top):
        # [1, 2, 3, 4, 5]
        print("Sorting stack ascending order (worst case)")
        sorted_stack(s)
        self.assertEqual(list(s), [1, 2, 3, 4, 5])

    def test_sort_stack_descending_order_best_case(self) -> None:
        # smallest items will be on top of stack. Basically,
        # already sorted.
        # with a stack in already sorted order, algorithm
        # will act the fastest.
        s: MyStack[T] = MyStack(5, 4, 3, 2, 1)
        # will look like this (leftmost is top of stack):
        # [1, 2, 3, 4]
        self.assertEqual(list(s), [1, 2, 3, 4, 5])
        # after sorting, should look like this (smallest values on top):
        # [1, 2, 3, 4]
        print("Sorting stack ascending order (best case)")
        sorted_stack(s)
        self.assertEqual(list(s), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
