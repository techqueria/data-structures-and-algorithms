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

    def insert_left(self, value: T) -> None:
        if not self.root:
            self.root = BTNode(value)
        else:
            self._insert_left(value, self.root, 1)

    def _insert_left(self, value: T, curr_node: BTNode[T], curr_depth: int) -> None:
        if not curr_node.left_child:
            curr_node.left_child = BTNode(value, curr_depth)
        elif not curr_node.right_child:
            curr_node.right_child = BTNode(value, curr_depth)
        elif value == curr_node.val:
            raise ValueError(f'Value {value} already exists in tree.')
        else:
            self._insert_left(value, curr_node.left_child, curr_depth + 1)

    def insert_right(self, value: T) -> None:
        if not self.root:
            self.root = BTNode(value)
        else:
            self._insert_right(value, self.root, 1)

    def _insert_right(self, value: T, curr_node: BTNode[T], curr_depth: int) -> None:
        if not curr_node.right_child:
            curr_node.right_child = BTNode(value, curr_depth)
        elif not curr_node.left_child:
            curr_node.left_child = BTNode(value, curr_depth)
        elif value == curr_node.val:
            raise ValueError(f'Value {value} already exists in tree.')
        else:
            self._insert_right(value, curr_node.right_child, curr_depth + 1)

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

@dataclass
class BinarySearchTree(BinaryTree[T]):

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


def _calculate_max_value_of_subtree(node: Optional[BTNode[T]], max_value: T) -> T:
    """This helper function will calculate the max value between
    the current node's value and its subtree.

    Args:
        node (Optional[BTNode[T]]): a binary tree node
        max_value (T): max value used to pass down to each node

    Returns:
        T: max value of left/right subtree and current node
    """
    if not node:
        return max_value
    else:
        return max(
            node.val,
            _calculate_max_value_of_subtree(node.left_child, max_value),
            _calculate_max_value_of_subtree(node.right_child, max_value)
        )

def _calculate_min_value_of_subtree(node: Optional[BTNode[T]], min_value: T) -> T:
    """Same as _calculate_max_value_of_subtree but min instead of max.

    Args:
        node (Optional[BTNode[T]]): binary tree node
        min_value (T): min value used to pass to each node

    Returns:
        T: min value of left/right subtree and current node
    """
    if not node:
        return min_value
    else:
        return min(
            node.val,
            _calculate_min_value_of_subtree(node.left_child, min_value),
            _calculate_min_value_of_subtree(node.right_child, min_value)
        )

def _validate_bst(node: Optional[BTNode[T]]) -> bool:
    """Helper function to validate_bst. Difference is,
    this function takes in a node rather than a binary tree
    instance. This will handle the logic for checking if we have
    a binary search tree or not.

    Args:
        node (Optional[BTNode[T]]): current node to validate left and right subtrees

    Returns:
        bool: True if bst properties are intact, False otherwise
    """
    if not node:
        # empty node is considered a binary search tree
        return True
    max_val_left_subtree = _calculate_max_value_of_subtree(node.left_child, node.val)
    min_val_right_subtree = _calculate_min_value_of_subtree(node.right_child, node.val)
    if max_val_left_subtree > node.val:
        return False
    if min_val_right_subtree < node.val:
        return False
    return _validate_bst(node.left_child) and _validate_bst(node.right_child)


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
    return _validate_bst(bt.root)

class TestBinarySearchTree(unittest.TestCase):

    def test_binary_search_tree_creation_height_3(self) -> None:
        bst: BinarySearchTree = BinarySearchTree()
        bst.insert(8)
        bst.insert(4)
        bst.insert(10)
        bst.insert(2)
        bst.insert(6)
        bst.insert(20)
        self.assertEqual(list(bst), [2, 4, 6, 8, 10, 20])
        self.assertEqual(bst.height(), 3)

    def test_binary_search_tree_creation_height_4(self) -> None:
        bst: BinarySearchTree = BinarySearchTree()
        bst.insert(8)
        bst.insert(2)
        bst.insert(10)
        bst.insert(4)
        bst.insert(6)
        bst.insert(20)
        self.assertEqual(list(bst), [2, 4, 6, 8, 10, 20])
        self.assertEqual(bst.height(), 4)


class TestValidateBST(unittest.TestCase):

    def test_validate_bst_true_case(self) -> None:
        bst: BinarySearchTree = BinarySearchTree()
        bst.insert(8)
        bst.insert(4)
        bst.insert(10)
        bst.insert(2)
        bst.insert(6)
        bst.insert(20)
        self.assertEqual(list(bst), [2, 4, 6, 8, 10, 20])
        self.assertEqual(bst.height(), 3)
        result = validate_bst(bst)
        self.assertEqual(result, True)

    def test_validate_bst_false_case_left_subtree(self) -> None:
        bt: BinaryTree = BinaryTree()
        bt.insert_left(8)
        bt.insert_left(4)
        bt.insert_left(10)
        bt.insert_left(2)
        bt.insert_left(1000)
        bt.insert_right(20)
        bt.insert_right(9)
        self.assertEqual(list(bt), [2, 4, 1000, 8, 9, 10, 20])
        self.assertEqual(bt.height(), 3)
        result = validate_bst(bt)
        self.assertEqual(result, False)

    def test_validate_bst_false_case_right_subtree(self) -> None:
        bt: BinaryTree = BinaryTree()
        bt.insert_left(8)
        bt.insert_left(4)
        bt.insert_left(10)
        bt.insert_left(2)
        bt.insert_left(1000)
        bt.insert_right(-100)
        bt.insert_right(9)
        self.assertEqual(list(bt), [2, 4, 1000, 8, 9, 10, -100])
        self.assertEqual(bt.height(), 3)
        result = validate_bst(bt)
        self.assertEqual(result, False)

    def test_calculate_max_value_of_subtree(self) -> None:
        bt: BinaryTree = BinaryTree()
        bt.insert_left(8)
        bt.insert_left(4)
        bt.insert_left(10)
        bt.insert_left(2)
        bt.insert_left(1000)
        bt.insert_right(20)
        bt.insert_right(9)
        # expected result of left subtree is be 1000
        result = _calculate_max_value_of_subtree(bt.root.left_child, bt.root.left_child.val)
        self.assertEqual(result, 1000)
        # expected result of overall max value is still 1000
        result = _calculate_max_value_of_subtree(bt.root, bt.root.val)
        self.assertEqual(result, 1000)
        # expected result of right subtree is 20
        result = _calculate_max_value_of_subtree(bt.root.right_child, bt.root.right_child.val)
        self.assertEqual(result, 20)

    def test_calculate_min_value_of_subtree(self) -> None:
        bt: BinaryTree = BinaryTree()
        bt.insert_left(8)
        bt.insert_left(4)
        bt.insert_left(10)
        bt.insert_left(2)
        bt.insert_left(1000)
        bt.insert_right(-100)
        bt.insert_right(9)
        # left subtree min should be 2
        result = _calculate_min_value_of_subtree(bt.root.left_child, bt.root.left_child.val)
        self.assertEqual(result, 2)
        # overall min value should be -100
        result = _calculate_min_value_of_subtree(bt.root, bt.root.val)
        self.assertEqual(result, -100)
        # right subtree min should be -100
        result = _calculate_min_value_of_subtree(bt.root.right_child, bt.root.right_child.val)
        self.assertEqual(result, -100)

if __name__ == '__main__':
    unittest.main()
