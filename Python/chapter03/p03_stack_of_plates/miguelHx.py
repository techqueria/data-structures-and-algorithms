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
from typing import List, Optional, Generator, Iterator

T = TypeVar('T')

@dataclass
class StackNode(Generic[T]):
    data: T
    next: 'Optional[StackNode[T]]'
    prev: 'Optional[StackNode[T]]'

class MyStackIterator(Generic[T], Iterator[T]):
    def __init__(self, top: Optional[StackNode[T]], bottom: Optional[StackNode[T]], size: int) -> None:
        self.forward_index = -1
        self.backward_index = size
        self._size = size
        self.current_node = top
        self.bottom_node = bottom

    def __next__(self) -> T:
        self.forward_index += 1
        if self.forward_index == self._size or self.current_node is None:
            self.forward_index = -1
            self.current_node = None
            raise StopIteration
        n: T = self.current_node.data
        self.current_node = self.current_node.next
        return n

    def __reversed__(self) -> T:
        self.backward_index -= 1
        if self.backward_index == -1 or self.bottom_node is None:
            self.backward_index = self._size
            self.bottom_node = None
            raise StopIteration
        n: T = self.bottom_node.data
        self.bottom_node = self.bottom_node.prev
        return n

class MyStack(Generic[T]):
    """Stack data structure implementation.
    Uses LIFO (last-in first-out) ordering.
    The most recent item added to the stack is
    the first removed.  Traversal is top to bottom.
    """

    def __init__(self) -> None:
        self.top: Optional[StackNode[T]] = None # top is a pointer to StackNode object
        self.bottom: Optional[StackNode[T]] = None
        self.size: int = 0
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
        if self.size > 1 and self.top:
            self.top.prev = None
        self.size -= 1
        return item

    def push(self, item: T) -> None:
        """
        Adds an item to the top of the stack
        Args:
            item (int): data we want at the top of stack
        """
        t = StackNode(item, None, None)
        t.next = self.top
        self.top = t
        if self.size == 0:
            self.bottom = t
        elif t.next:
            t.next.prev = t
        self.size += 1

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

    def __iter__(self) -> Iterator[T]:
        """
        Builds a list of the current stack state.
        For example, given the following stack:
            3 -> 2 -> 1, where 3 is the top,
        Expect:
            [3, 2, 1]
        Returns:
            List[int]: list of integers
        """
        return MyStackIterator(self.top, self.bottom, self.size)

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
    
    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        if self.size == 0:
            return '<Empty>'
        values = []
        n = self.top
        while n and n.next:
            values.append(str(n.data))
            n = n.next
        if n:
            values.append(str(n.data))
        return '->'.join(values)


def yield_set_of_stacks(stack_list: List[MyStack[T]]) -> Generator[T, None, None]:
    stack: MyStack[T]
    for stack in reversed(stack_list):
        for item in stack:
            yield item

class SetofStacks(Generic[T]):
    def __init__(self) -> None:
        self.set_of_stacks: List[MyStack[T]] = []
        self.stack_threshold: int = 3
        self.size: int = 0
    
    def push(self, item: T) -> None:
        # threshold check
        if (not self.set_of_stacks) or len(self.set_of_stacks[-1]) >= self.stack_threshold:
            # create new stack
            self.set_of_stacks.append(MyStack())
        self.set_of_stacks[-1].push(item)
        self.size += 1
        return
    
    def _pop(self) -> T:
        return self.set_of_stacks[-1].pop()
    
    def _pop_stack(self) -> MyStack[T]:
        return self.set_of_stacks.pop(-1)

    def pop(self) -> T:
        """Removes element off of the current stack.
        We will only pop a stack if the current stack
        contains a single value
        Returns:
            T: popped item
        """
        if len(self.set_of_stacks[-1]) > 1:
            item: T = self._pop()
        else:
            s: MyStack[T] = self._pop_stack()
            item = s.pop()
        self.size -= 1
        return item
    
    def peek(self) -> T:
        return self.set_of_stacks[-1].peek()
    
    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Generator[T, None, None]:
        return yield_set_of_stacks(self.set_of_stacks)


class TestSetofStacks(unittest.TestCase):

    def test_setofstacks_push_and_peek(self) -> None:
        sos = SetofStacks()
        self.assertEqual(len(sos), 0)
        sos.push(5)
        self.assertEqual(len(sos), 1)
        self.assertEqual(sos.peek(), 5)
        sos.push(6)
        self.assertEqual(len(sos), 2)
        self.assertEqual(sos.peek(), 6)
        sos.push(7)
        self.assertEqual(len(sos), 3)
        self.assertEqual(sos.peek(), 7)

        # with threshold of 3 (default),
        # verify that a new stack is created
        # after the next push
        sos.push(8)
        # [5->6->7->, 8->] new stack created because threshold is 3
        self.assertEqual(len(sos), 4)
        self.assertEqual(sos.peek(), 8)
        self.assertEqual(sos.set_of_stacks[1].peek(), 8)
        self.assertEqual(len(sos.set_of_stacks[1]), 1)
    
    def test_setofstacks_pop(self) -> None:
        # pop empty stack
        sos = SetofStacks()
        with self.assertRaises(IndexError):
            sos.pop()
        sos.push(1)
        sos.push(2)
        sos.push(3)
        # size is 3
        self.assertEqual(len(sos), 3)
        val = sos.pop()
        self.assertEqual(val, 3)
        self.assertEqual(len(sos), 2) # size should now be 2
        sos.push(3)
        sos.push(4) # new stack created, verify that pop works as intended
        self.assertEqual(len(sos), 4)
        val = sos.pop()
        self.assertEqual(val, 4)
        self.assertEqual(len(sos), 3)

    def test_setofstacks_pop_three_stacks(self) -> None:
        s = SetofStacks()
        # No stacks exists in set, yet
        self.assertEqual(len(s.set_of_stacks), 0)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(len(s.set_of_stacks), 1)
        # threshold met, should be two after next push
        s.push(4)
        # should be 2 stacks now
        self.assertEqual(len(s.set_of_stacks), 2)
        s.push(5)
        s.push(6)
        self.assertEqual(len(s.set_of_stacks), 2)
        s.push(7)
        self.assertEqual(len(s.set_of_stacks), 3)
        s.push(8)
        s.push(9)
        self.assertEqual(len(s.set_of_stacks), 3)
        s.push(10)
        # should be four stacks now
        self.assertEqual(len(s.set_of_stacks), 4)
        self.assertEqual(list(s), [10, 9, 8 , 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(len(s), 10)
        val = s.pop()
        self.assertEqual(len(s.set_of_stacks), 3)
        self.assertEqual(val, 10)
        self.assertEqual(len(s), 9)
        self.assertEqual(list(s), [9, 8 , 7, 6, 5, 4, 3, 2, 1])
        val = s.pop()
        # length of stacks should still be 3
        self.assertEqual(len(s.set_of_stacks), 3)
        self.assertEqual(val, 9)
        self.assertEqual(len(s), 8)
        self.assertEqual(list(s), [8, 7, 6, 5, 4, 3, 2, 1])
        val = s.pop()
        # after this pop, should still have 3
        self.assertEqual(len(s.set_of_stacks), 3)
        self.assertEqual(val, 8)
        self.assertEqual(len(s), 7)
        self.assertEqual(list(s), [7, 6, 5, 4, 3, 2, 1])
        val = s.pop()
        self.assertEqual(len(s.set_of_stacks), 2)
        self.assertEqual(val, 7)
        self.assertEqual(len(s), 6)
        self.assertEqual(list(s), [6, 5, 4, 3, 2, 1])
        val = s.pop()
        self.assertEqual(len(s.set_of_stacks), 2)
        self.assertEqual(val, 6)
        self.assertEqual(len(s), 5)
        self.assertEqual(list(s), [5, 4, 3, 2, 1])
        val = s.pop()
        self.assertEqual(len(s.set_of_stacks), 2)
        self.assertEqual(val, 5)
        self.assertEqual(len(s), 4)
        self.assertEqual(list(s), [4, 3, 2, 1])
        val = s.pop()
        self.assertEqual(len(s.set_of_stacks), 1)
        self.assertEqual(val, 4)
        self.assertEqual(len(s), 3)
        self.assertEqual(list(s), [3, 2, 1])
        val = s.pop()
        self.assertEqual(len(s.set_of_stacks), 1)
        self.assertEqual(val, 3)
        self.assertEqual(len(s), 2)
        self.assertEqual(list(s), [2, 1])


class TestMyStack(unittest.TestCase):
    def test_stack_push(self) -> None:
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

    def test_stack_peek(self) -> None:
        s = MyStack()
        with self.assertRaises(IndexError):
            s.peek()
        s.push(1)
        s.push(2)
        s.push(99)
        top_val = s.peek()
        self.assertEqual(top_val, 99)

    def test_stack_pop(self) -> None:
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

    def test__bool__(self) -> None:
        s = MyStack()
        self.assertFalse(s)
        s.push(3)
        self.assertTrue(s)


if __name__ == '__main__':
    unittest.main()
