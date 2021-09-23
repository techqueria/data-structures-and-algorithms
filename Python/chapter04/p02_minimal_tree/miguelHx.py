"""Python Version 3.9.2
4.2 - Minimal Tree:
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
"""
import math
import unittest

from abc import abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar
from typing import Optional, Protocol
from typing import Generator, List


T = TypeVar('T', bound='Comparable')

class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, other: T) -> bool:
        pass

    @abstractmethod
    def __gt__(self, other: T) -> bool:
        pass

    @abstractmethod
    def __eq__(self, other: T) -> bool:
        pass

@dataclass
class BSTNode:
    val: int
    left_child: 'Optional[BSTNode]' = None
    right_child: 'Optional[BSTNode]' = None

    def __str__(self):
        return f'Node ({self.id}), Left ID: {self.left_child.id}, Right ID: {self.right_child.id}'

class BSTIterator:

    def __init__(self, root: BSTNode):
        self.gen = self.in_order_traversal_generator(root)

    def in_order_traversal_generator(self, node: BSTNode) -> Generator:
        if node.left_child:
            yield from self.in_order_traversal_generator(node.left_child)
        yield node.val
        if node.right_child:
            yield from self.in_order_traversal_generator(node.right_child)

    def __next__(self) -> T:
        return next(self.gen)

@dataclass
class BinarySearchTree:
    root: 'Optional[BSTNode]' = None

    def insert(self, value: T) -> None:
        if not self.root:
            self.root = BSTNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value: T, curr_node: BSTNode) -> None:
        if value < curr_node.val:
            if not curr_node.left_child:
                # insert here
                curr_node.left_child = BSTNode(value)
            else:
                # otherwise, keep searching left subtree
                self._insert(value, curr_node.left_child)
        elif value > curr_node.val:
            if not curr_node.right_child:
                # insert here
                curr_node.right_child = BSTNode(value)
            else:
                # otherwise, keep searching right subtree
                self._insert(value, curr_node.right_child)
        else:
            raise ValueError(f'Value {value} already exists in tree.')

    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node: Optional[BSTNode]) -> int:
        if not node:
            return 0
        else:
            return 1 + max(self._height(node.left_child), self._height(node.right_child))

    def print_tree(self):
        if self.root:
            self._print_tree(self.root)

    def _print_tree(self, curr_node: BSTNode) -> None:
        if curr_node:
            self._print_tree(curr_node.left_child)
            print(curr_node.val)
            self._print_tree(curr_node.right_child)

    def __iter__(self) -> Generator:
        return BSTIterator(self.root)



def minimal_tree(arr: List[T], bst: Optional[BinarySearchTree] = None) -> BinarySearchTree:
    """Given a sorted (increasing order) array
    with unique integer elements, write an algorithm
    to create a binary search tree with minimal height.
    Basic steps:
    1. get midpoint
    2. insert midpoint into bst
    3. turn left to get left midpoint until no more values
    4. turn right to insert right midpoint until no more values

    Time Complexity: O(n) where n is size of arr
    Space Complexity: O(n)

    Args:
        arr (List[T]): list of unique numbers sorted, in incr. order.

    Returns:
        BinarySearchTree: A binary search tree with minimal height.
    """
    bst = BinarySearchTree() if not bst else bst
    if not arr:
        return bst
    # middle value gets inserted first before going left or right
    middle = math.floor(len(arr) / 2)
    bst.insert(arr[middle])
    left_subarr = arr[:middle]
    right_subarr = arr[middle+1:]
    minimal_tree(left_subarr, bst)
    minimal_tree(right_subarr, bst)
    return bst


class TestBinarySearchTree(unittest.TestCase):

    def test_binary_search_tree_creation_height_3(self):
        bst = BinarySearchTree()
        bst.insert(8)
        bst.insert(4)
        bst.insert(10)
        bst.insert(2)
        bst.insert(6)
        bst.insert(20)
        self.assertEqual(list(bst), [2, 4, 6, 8, 10, 20])
        self.assertEqual(bst.height(), 3)

    def test_binary_search_tree_creation_height_4(self):
        bst = BinarySearchTree()
        bst.insert(8)
        bst.insert(2)
        bst.insert(10)
        bst.insert(4)
        bst.insert(6)
        bst.insert(20)
        self.assertEqual(list(bst), [2, 4, 6, 8, 10, 20])
        self.assertEqual(bst.height(), 4)


class TestMinimalTree(unittest.TestCase):

    def test_minimal_tree(self):
        # sorted, increasing order array
        arr = [2, 4, 6, 8, 9, 10, 20]
        bst = minimal_tree(arr)
        self.assertEqual(list(bst), [2, 4, 6, 8, 9, 10, 20])
        self.assertEqual(bst.height(), 3)


if __name__ == '__main__':
    unittest.main()
