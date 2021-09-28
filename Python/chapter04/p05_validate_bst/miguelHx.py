"""Python Version 3.9.2
4.5 - Validate BST:
Implement a function to check if a binary tree
is balanced. For the purposes of this question,
a balanced tree is defined tto be a tree such that
the heights of the two subtrees of any node never
differ by more than one.
"""
import unittest

from abc import abstractmethod
from collections import deque
from dataclasses import dataclass
from typing import Generic, TypeVar, Dict
from typing import Optional, Protocol, Deque
from typing import Generator, List, Iterator


T = TypeVar('T', bound='Comparable')

class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, other: T) -> bool:
        pass

    @abstractmethod
    def __gt__(self, other: T) -> bool:
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        pass

@dataclass
class BTNode(Generic[T]):
    val: T
    depth: int = 0
    left_child: 'Optional[BTNode[T]]' = None
    right_child: 'Optional[BTNode[T]]' = None

    @property
    def children(self) -> 'List[Optional[BTNode[T]]]':
        return [self.left_child, self.right_child]

    def children_as_str(self) -> str:
        return ', '.join(str(child.val) if child else '' for child in self.children)

    def __str__(self) -> str:
        return f'Node ({self.val}), children: {self.children_as_str()}'

class BTIterator(Iterator[T]):

    def __init__(self, root: Optional[BTNode[T]]):
        self.gen = self.in_order_traversal_generator(root)

    def in_order_traversal_generator(self, node: Optional[BTNode[T]]) -> Generator[T, Optional[BTNode[T]], None]:
        if not node:
            raise StopIteration
        if node.left_child:
            yield from self.in_order_traversal_generator(node.left_child)
        yield node.val
        if node.right_child:
            yield from self.in_order_traversal_generator(node.right_child)

    def __next__(self) -> T:
        return next(self.gen)

@dataclass
class BinaryTree(Generic[T]):
    root: 'Optional[BTNode[T]]' = None

    def insert(self, value: T) -> None:
        if not self.root:
            self.root = BTNode(value)
        else:
            self._insert(value, self.root, 1)

    def _insert(self, value: T, curr_node: BTNode[T], curr_depth: int) -> None:
        if value < curr_node.val:
            if not curr_node.left_child:
                # insert here
                curr_node.left_child = BTNode(value, curr_depth)
            else:
                # otherwise, keep searching left subtree
                self._insert(value, curr_node.left_child, curr_depth + 1)
        elif value > curr_node.val:
            if not curr_node.right_child:
                # insert here
                curr_node.right_child = BTNode(value, curr_depth)
            else:
                # otherwise, keep searching right subtree
                self._insert(value, curr_node.right_child, curr_depth + 1)
        else:
            raise ValueError(f'Value {value} already exists in tree.')

    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node: Optional[BTNode[T]]) -> int:
        if not node:
            return 0
        else:
            return 1 + max(self._height(node.left_child), self._height(node.right_child))

    def print_tree(self) -> None:
        if self.root:
            self._print_tree(self.root)

    def _print_tree(self, curr_node: Optional[BTNode[T]]) -> None:
        if curr_node:
            self._print_tree(curr_node.left_child)
            print(curr_node.val)
            self._print_tree(curr_node.right_child)

    def __iter__(self) -> BTIterator[T]:
        return BTIterator(self.root)



def validate_bst(bt: BinaryTree[T]) -> bool:
    """This function will check if the input
    binary tree is a binary search tree.
    In order for a binary tree to be a binary search
    tree, the following conditions must be true for every 
    node in the tree:
    The left subtree of a node contains only nodes with keys
    lesser than the node's key.
    The right subtree of a node contains only nodes with keys
    greater than the node's key.
    The left and right subtree each must also be a binary search
    tree.

    Args:
        bt (BinaryTree[T]): Input binary tree, we will start at root

    Returns:
        bool: True if tree is a binary search tree, False otherwise
    """
    return False

class TestBinarySearchTree(unittest.TestCase):

    def test_binary_search_tree_creation_height_3(self) -> None:
        bt: BinaryTree = BinaryTree()
        bt.insert(8)
        bt.insert(4)
        bt.insert(10)
        bt.insert(2)
        bt.insert(6)
        bt.insert(20)
        self.assertEqual(list(bt), [2, 4, 6, 8, 10, 20])
        self.assertEqual(bt.height(), 3)

    def test_binary_search_tree_creation_height_4(self) -> None:
        bt: BinaryTree = BinaryTree()
        bt.insert(8)
        bt.insert(2)
        bt.insert(10)
        bt.insert(4)
        bt.insert(6)
        bt.insert(20)
        self.assertEqual(list(bt), [2, 4, 6, 8, 10, 20])
        self.assertEqual(bt.height(), 4)


class TestValidateBST(unittest.TestCase):

    def test_validate_bst_true_case(self) -> None:
        bt: BinaryTree = BinaryTree()
        bt.insert(8)
        bt.insert(4)
        bt.insert(10)
        bt.insert(2)
        bt.insert(6)
        bt.insert(20)
        self.assertEqual(list(bt), [2, 4, 6, 8, 10, 20])
        self.assertEqual(bt.height(), 3)

        result = validate_bst(bt)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
