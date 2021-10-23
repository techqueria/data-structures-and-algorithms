"""Python Version 3.9.2
4.6 - Successor:
Write an algorithm to find the "next" node
(i.e., in-order successor) of a given node
in a binary search tree. You may assume that each
node has a link to its parent.
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
    parent: 'Optional[BTNode[T]]' = None

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
            curr_node.left_child.parent = curr_node
        elif not curr_node.right_child:
            curr_node.right_child = BTNode(value, curr_depth)
            curr_node.right_child.parent = curr_node
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
            curr_node.right_child.parent = curr_node
        elif not curr_node.left_child:
            curr_node.left_child = BTNode(value, curr_depth)
            curr_node.left_child.parent = curr_node
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
                curr_node.left_child.parent = curr_node
            else:
                # otherwise, keep searching left subtree
                self._insert(value, curr_node.left_child, curr_depth + 1)
        elif value > curr_node.val:
            if not curr_node.right_child:
                # insert here
                curr_node.right_child = BTNode(value, curr_depth)
                curr_node.right_child.parent = curr_node
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


def successor(node: BTNode[T]) -> Optional[BTNode[T]]:
    """This function will find the "next" node
    (i.e., in-order successor) of a given node in 
    a binary search tree.
    The in-order successor of an input node can be defined
    as the next node in in-order traversal of the binary tree.
    In-order successor is NULL for the last node in in-order
    traversal.

    If the right subtree of the input node is not None, then
    the successor will lie in the right subtree.

    If the right subtree of the input node is None, then the
    successor is one of the ancestors. That is, the parent
    of the first node up the parent chain where that node is the
    left child of its parent.

    Args:
        node (BTNode[T]): node of interest

    Returns:
        Optional[BTNode[T]]: successor to input node
    """

    # first, check right subtree
    if node.right_child:
        return _calculate_min_value_of_subtree(node, node.val)
    
    # otherwise, go up the parent tree

    pass


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


class TestSubtreeMinMax(unittest.TestCase):

    def test_calculate_max_value_of_subtree(self) -> None:
        bt: BinaryTree = BinaryTree()
        bt.insert_left(8)
        bt.insert_left(4)
        bt.insert_left(10)
        bt.insert_left(2)
        bt.insert_left(1000)
        bt.insert_right(20)
        bt.insert_right(9)
        if not bt.root or not bt.root.left_child or not bt.root.right_child:
            raise Exception("bt.root or one of it's children is empty for this test case.")
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
        if not bt.root or not bt.root.left_child or not bt.root.right_child:
            raise Exception("bt.root or one of it's children is empty for this test case.")
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
