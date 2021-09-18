"""Python Version 3.9.2
4.2 - Minimal Tree:
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
"""
import unittest

from abc import abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar
from typing import Optional, Protocol
from typing import Generator


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
    root: 'Optional[BSTNode]'

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


class TestBinarySearchTree(unittest.TestCase):

    def test_binary_search_tree_creation(self):
        bst = BinarySearchTree(None)
        bst.insert(8)
        bst.insert(4)
        bst.insert(10)
        bst.insert(2)
        bst.insert(6)
        bst.insert(20)
        self.assertEqual(list(bst), [2, 4, 6, 8, 10, 20])


if __name__ == '__main__':
    unittest.main()
