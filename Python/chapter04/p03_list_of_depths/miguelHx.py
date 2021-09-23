"""Python Version 3.9.2
4.3 - List of Depths:
Given a binary tree, design an algorithm which creates
a linked list of all the nodes at each depth
(e.g., if you have a tree with depth D, you'll have D linked lists).
"""
import unittest

from abc import abstractmethod
from collections import deque
from dataclasses import dataclass
from typing import Generic, TypeVar
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
    left_child: 'Optional[BTNode]' = None
    right_child: 'Optional[BTNode]' = None

    def __str__(self):
        return f'Node ({self.id}), Left ID: {self.left_child.id}, Right ID: {self.right_child.id}'

class BSTIterator(Iterator[T]):

    def __init__(self, root: Optional[BTNode]):
        self.gen = self.in_order_traversal_generator(root)

    def in_order_traversal_generator(self, node: Optional[BTNode]) -> Generator:
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
class BinaryTree:
    root: 'Optional[BTNode]' = None

    def insert(self, value: T) -> None:
        if not self.root:
            self.root = BTNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value: T, curr_node: BTNode) -> None:
        if value < curr_node.val:
            if not curr_node.left_child:
                # insert here
                curr_node.left_child = BTNode(value)
            else:
                # otherwise, keep searching left subtree
                self._insert(value, curr_node.left_child)
        elif value > curr_node.val:
            if not curr_node.right_child:
                # insert here
                curr_node.right_child = BTNode(value)
            else:
                # otherwise, keep searching right subtree
                self._insert(value, curr_node.right_child)
        else:
            raise ValueError(f'Value {value} already exists in tree.')

    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node: Optional[BTNode]) -> int:
        if not node:
            return 0
        else:
            return 1 + max(self._height(node.left_child), self._height(node.right_child))

    def print_tree(self):
        if self.root:
            self._print_tree(self.root)

    def _print_tree(self, curr_node: Optional[BTNode]) -> None:
        if curr_node:
            self._print_tree(curr_node.left_child)
            print(curr_node.val)
            self._print_tree(curr_node.right_child)

    def __iter__(self) -> BSTIterator:
        return BSTIterator(self.root)


def list_of_depths(bt: BinaryTree) -> List[Deque[BTNode]]:
    """Given a binary tree, design an algorithm which creates
    a linked list of all the nodes at each depth
    (e.g., if you have a tree with depth D, you'll have D linked lists).
    Args:
        bst (BinaryTree): input binary tree

    Returns:
        List[Deque[BTNode]]: list of nodes at each depth
    """
    return []



class TestBinaryTree(unittest.TestCase):

    def test_binary_search_tree_creation_height_3(self):
        bt = BinaryTree()
        bt.insert(8)
        bt.insert(4)
        bt.insert(10)
        bt.insert(2)
        bt.insert(6)
        bt.insert(20)
        self.assertEqual(list(bt), [2, 4, 6, 8, 10, 20])
        self.assertEqual(bt.height(), 3)

    def test_binary_search_tree_creation_height_4(self):
        bt = BinaryTree()
        bt.insert(8)
        bt.insert(2)
        bt.insert(10)
        bt.insert(4)
        bt.insert(6)
        bt.insert(20)
        self.assertEqual(list(bt), [2, 4, 6, 8, 10, 20])
        self.assertEqual(bt.height(), 4)


class TestListOfDepths(unittest.TestCase):

    def test_list_of_depths_full_btree_height_3(self):
        bt = BinaryTree()
        bt.insert(8)
        bt.insert(4)
        bt.insert(10)
        bt.insert(2)
        bt.insert(6)
        bt.insert(20)
        self.assertEqual(list(bt), [2, 4, 6, 8, 10, 20])
        self.assertEqual(bt.height(), 3)

        expected_result = [
            deque([8]),
            deque([4, 10]),
            deque([2, 6, 9, 10])
        ]

        result = list_of_depths(bt)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
