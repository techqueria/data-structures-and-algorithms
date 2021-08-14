"""Python version 3.7.0
3.1 - Three in one
Describe how you could use a single array to implement three stacks
"""

import copy
import unittest

from dataclasses import dataclass
from typing import Generic, TypeVar
from typing import List, Optional

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


class StackTrio:

    def __init__(self, stack_capacity = 7):
        self.num_stacks = 3
        self.stack_capacity = stack_capacity
        self.stack_info = {
            1: {
                'start': 0,
                'end': stack_capacity - 1,
                'size': 0,
                'top_index': 0,
                'top_index_next': -1, # index after top, initially starts at a sentinel value because the stack is empty, so there is no "next"
            },
            2: {
                'start': stack_capacity,
                'end': stack_capacity * 2 - 1,
                'size': 0,
                'top_index': stack_capacity,
                'top_index_next': -1,
            },
            3: {
                'start': stack_capacity * 2,
                'end': stack_capacity * 3 - 1,
                'size': 0,
                'top_index': stack_capacity * 2,
                'top_index_next': -1
            }
        }
        self.values = [0] * (stack_capacity * self.num_stacks)

    def is_empty(self, stack_id):
        return self.stack_info[stack_id]['size'] <= 0
    
    def peek(self, stack_id):
        # this method returns the value at the top index
        if self.is_empty(stack_id):
            raise IndexError('Stack is empty. Stack ID: {}'.format(stack_id))
        return self.values[self.stack_info[stack_id]['top_index']]

    def push(self, stack_id, value):
        # first, check if stack of interest is full
        if self.stack_info[stack_id]['size'] >= self.stack_capacity:
            raise IndexError('Stack is full. Stack ID: {}'.format(stack_id))

        

        stack_top_index = self.stack_info[stack_id]['top_index']
        new_stack_top_index = stack_top_index + 1
        # if empty, then top index and next index stay the same.
        if self.is_empty(stack_id):
            self.values[stack_top_index] = value
            # update stack size.
            self.stack_info[stack_id]['size'] += 1
            return

        # otherwise, stack is not empty, and so we
        # first need to update the next and top indices, then update
        # the values accordingly.
        self.stack_info[stack_id]['top_index_next'] = stack_top_index
        self.stack_info[stack_id]['top_index'] = new_stack_top_index
        self.values[new_stack_top_index] = value
        self.stack_info[stack_id]['size'] += 1
        
        
    
    def pop(self, stack_id):
        # first, make sure we are not at an empty stack
        if self.is_empty(stack_id):
            raise IndexError('Stack is empty. Stack ID: {}'.format(stack_id))
        # if there is one element, top index will be 0
        # and next index will be -1
        # if there are two elements, top index will be 1,
        # and next index will be 0
        # if there are three elements, top index will be 2,
        # next will be 1
        # basically, the next index will be one less than top index

        # when we pop, top index will become next, and next will get
        # decremented by one. (Or, each get decremented by 1)

        # get stack top index, then set value to 0 as a way of clearing
        original_stack_top_index = self.stack_info[stack_id]['top_index']
        val_before_pop = self.peek(stack_id)

        # special case, when there is only one element in this stack,
        # we will clear top index, and reset next to sentinel value (-1)

        if self.get_size(stack_id) == 1:
            self.values[original_stack_top_index] = 0
            # top index should stay the same, but will reset next index to sentinel value (-1)
            self.stack_info[stack_id]['top_index_next'] = -1
            self.stack_info[stack_id]['size'] -= 1
            return val_before_pop

        
        # otherwise, stack size is greater than 2, and we can decrement
        # top index and next index by 1
        self.stack_info[stack_id]['top_index'] -= 1
        # if stack size is 2, then we want to prevent underflow of next index
        if self.get_size(stack_id) == 2:
            self.stack_info[stack_id]['top_index_next'] = -1
        else:
            self.stack_info[stack_id]['top_index_next'] -= 1
        # clear value
        self.values[original_stack_top_index] = 0
        # decrement size
        self.stack_info[stack_id]['size'] -= 1
        return val_before_pop
    
    def get_size(self, stack_id):
        return self.stack_info[stack_id]['size']
    
    def __str__(self):
        """
        We will print out the values
        as well as the stack info for each stack
        """
        d = copy.deepcopy(self.stack_info)
        d['values'] = str(self.values)
        return str(d)
        


        


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




class TestThreeInOne(unittest.TestCase):
    
    def test_stack_push(self):

        s_trio = StackTrio()

        self.assertEqual(s_trio.get_size(1), 0)
        self.assertEqual(s_trio.get_size(2), 0)
        self.assertEqual(s_trio.get_size(3), 0)

        s_trio.push(1, 99)

        self.assertEqual(s_trio.get_size(1), 1)
        self.assertEqual(s_trio.get_size(2), 0)
        self.assertEqual(s_trio.get_size(3), 0)

        s_trio.push(1, 100)
        self.assertEqual(s_trio.get_size(1), 2)
        self.assertEqual(s_trio.get_size(2), 0)
        self.assertEqual(s_trio.get_size(3), 0)

        s_trio.push(2, 101)

        self.assertEqual(s_trio.get_size(1), 2)
        self.assertEqual(s_trio.get_size(2), 1)
        self.assertEqual(s_trio.get_size(3), 0)

        s_trio.push(2, 102)
        self.assertEqual(s_trio.get_size(1), 2)
        self.assertEqual(s_trio.get_size(2), 2)
        self.assertEqual(s_trio.get_size(3), 0)

        s_trio.push(3, 103)

        self.assertEqual(s_trio.get_size(1), 2)
        self.assertEqual(s_trio.get_size(2), 2)
        self.assertEqual(s_trio.get_size(3), 1)

        s_trio.push(3, 104)
        self.assertEqual(s_trio.get_size(1), 2)
        self.assertEqual(s_trio.get_size(2), 2)
        self.assertEqual(s_trio.get_size(3), 2)

    
    def test_stack_peek(self):
        s_trio = StackTrio()

        self.assertRaises(IndexError, lambda: s_trio.peek(1))
        self.assertRaises(IndexError, lambda: s_trio.peek(2))
        self.assertRaises(IndexError, lambda: s_trio.peek(3))

        s_trio.push(1, 99)
        self.assertEqual(s_trio.peek(1), 99)
        s_trio.push(1, 100)
        self.assertEqual(s_trio.peek(1), 100)
        s_trio.push(1, 101)
        self.assertEqual(s_trio.peek(1), 101)
        
        # test that peek still works after popping
        val = s_trio.pop(1)
        self.assertEqual(val, 101)
        self.assertEqual(s_trio.peek(1), 100)
        return
    
    def test_stack_is_empty(self):
        s = MyStack()
        self.assertTrue(s.is_empty())
        s.push(7)
        self.assertFalse(s.is_empty())
    
    def test_stack_pop(self):
        # first case, attempt to pop an empty stack
        s_trio = StackTrio()
        self.assertRaises(IndexError, lambda: s_trio.pop(1))
        self.assertRaises(IndexError, lambda: s_trio.pop(2))
        self.assertRaises(IndexError, lambda: s_trio.pop(3))

        # next, test out pop for each stack
        s_trio.push(1, 199)
        s_trio.push(2, 299)
        s_trio.push(3, 399)

        self.assertEqual(s_trio.get_size(1), 1)
        self.assertEqual(s_trio.get_size(2), 1)
        self.assertEqual(s_trio.get_size(3), 1)

        val = s_trio.pop(1)
        self.assertEqual(val, 199)
        self.assertEqual(s_trio.get_size(1), 0)
        
        s_trio.push(1, 199)
        s_trio.push(1, 200)

        val = s_trio.pop(1)
        self.assertEqual(val, 200)
        self.assertEqual(s_trio.get_size(1), 1)

        val = s_trio.pop(2)
        self.assertEqual(val, 299)
        self.assertEqual(s_trio.get_size(2), 0)

        s_trio.push(2, 299)
        s_trio.push(2, 300)

        val = s_trio.pop(2)

        self.assertEqual(val, 300)
        self.assertEqual(s_trio.get_size(2), 1)

        val = s_trio.pop(3)

        self.assertEqual(val, 399)
        self.assertEqual(s_trio.get_size(3), 0)

        s_trio.push(3, 399)
        s_trio.push(3, 400)

        self.assertEqual(s_trio.get_size(3), 2)

        val = s_trio.pop(3)

        self.assertEqual(val, 400)
        self.assertEqual(s_trio.get_size(3), 1)
    

if __name__ == '__main__':
    unittest.main()
