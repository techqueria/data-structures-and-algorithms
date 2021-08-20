"""Python version 3.7.0
3.1 - Three in one
Describe how you could use a single array to implement three stacks
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

@dataclass
class StackInfo:
    id: int
    start: int
    end: int
    size: int
    top_index: int
    top_index_next: int


class StackTrio:

    def __init__(self, stack_capacity = 7):
        self.num_stacks = 3
        self.stack_capacity = stack_capacity
        first_stack_info = StackInfo(
            id: 1,
            start_index: 0,
            end_index: stack_capacity - 1,
            size: 0,
            top_index: 0,
            top_next_index: -1
        )
        second_stack_info = StackInfo(
            2, # id
            stack_capacity, # start index
            stack_capacity * 2 - 1, # end index
            0, # size
            stack_capacity, # top index
            -1 # top index next
        )
        third_stack_info = StackInfo(
            3, # id
            stack_capacity * 2, # start index
            stack_capacity * 3 - 1, # end index
            0, # size
            stack_capacity * 2, # top index
            -1 # top index next
        )
        self.stack_info = {
            1: first_stack_info,
            2: second_stack_info,
            3: third_stack_info
        }
        self.values = [0] * (stack_capacity * self.num_stacks)
    
    def _validate_stack_id(self, stack_id: int):
        """Helper method to make sure stack_id
        doesn't go out of range.

        Args:
            stack_id (int): id used to refer to correct stack valid ids: 1-3
        """
        if stack_id < 1 or stack_id > 3:
            raise IndexError(f'Stack Id out of range. Valid ranges: 1-3, input: {stack_id}')

    def is_empty(self, stack_id: int):
        self._validate_stack_id(stack_id)
        return self.stack_info[stack_id].size <= 0
    
    def peek(self, stack_id):
        # this method returns the value at the top index
        self._validate_stack_id(stack_id)
        if self.is_empty(stack_id):
            raise IndexError('Stack is empty. Stack ID: {}'.format(stack_id))
        return self.values[self.stack_info[stack_id].top_index]

    def push(self, stack_id, value):
        self._validate_stack_id(stack_id)
        # then, check if stack of interest is full
        if self.stack_info[stack_id].size >= self.stack_capacity:
            raise IndexError('Stack is full. Stack ID: {}'.format(stack_id))
        stack_top_index = self.stack_info[stack_id].top_index
        new_stack_top_index = stack_top_index + 1
        # if empty, then top index and next index stay the same.
        if self.is_empty(stack_id):
            self.values[stack_top_index] = value
            # update stack size.
            self.stack_info[stack_id].size += 1
            return

        # otherwise, stack is not empty, and so we
        # first need to update the next and top indices, then update
        # the values accordingly.
        self.stack_info[stack_id].top_index_next = stack_top_index
        self.stack_info[stack_id].top_index = new_stack_top_index
        self.values[new_stack_top_index] = value
        self.stack_info[stack_id].size += 1
        
        
    
    def pop(self, stack_id):
        self._validate_stack_id(stack_id)
        # then, make sure we are not at an empty stack
        if self.is_empty(stack_id):
            raise IndexError('Stack is empty. Stack ID: {}'.format(stack_id))
        # basically, the next index will be one less than top index.
        # when we pop, each top index will get decremented by 1
        original_stack_top_index = self.stack_info[stack_id].top_index
        val_before_pop = self.peek(stack_id)
        self.stack_info[stack_id].top_index -= 1
        self.stack_info[stack_id].top_index_next -= 1
        # clear value
        self.values[original_stack_top_index] = 0
        # decrement size
        self.stack_info[stack_id].size -= 1
        return val_before_pop
    
    def get_size(self, stack_id):
        self._validate_stack_id(stack_id)
        return self.stack_info[stack_id].size
    
    def __str__(self):
        """
        We will print out the values
        as well as the stack info for each stack
        """
        d = copy.deepcopy(self.stack_info)
        d['values'] = str(self.values)
        return str(d)


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
    
    def test_validate_stack_id(self):
        s_trio = StackTrio()
        self.assertRaises(IndexError, lambda: s_trio._validate_stack_id(4))
        self.assertRaises(IndexError, lambda: s_trio._validate_stack_id(0))
    

if __name__ == '__main__':
    unittest.main()
