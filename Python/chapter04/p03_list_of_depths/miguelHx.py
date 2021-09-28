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


def list_of_depths(bt: BinaryTree[T]) -> Dict[int, Deque[T]]:
    """Given a binary tree, design an algorithm which creates
    a linked list of all the nodes at each depth
    (e.g., if you have a tree with depth D, you'll have D linked lists).

    Note: The original problem statement said to return a list of nodes for
    each depth. However, I am instead creating a list of node vals for each depth.

    Args:
        bt (BinaryTree): input binary tree

    Returns:
        List[Deque[BTNode]]: list of nodes at each depth
    """
    if not bt.root:
        return {}
    # first, what is depth of tree?
    total_depth = bt.height()
    depth_list_map: Dict[int, Deque[T]] = {
        0: deque([bt.root.val])
    }
    # initialize
    for d in range(1, total_depth):
        depth_list_map[d] = deque()
    queue: Deque[BTNode[T]] = deque([bt.root])
    # root is depth 0
    while queue:
        bt_node = queue.popleft()
        for n in bt_node.children:
            if not n:
                continue
            # otherwise,
            queue.append(n)
            depth_list_map[n.depth].append(n.val)
    return depth_list_map


class TestBinaryTree(unittest.TestCase):

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


class TestListOfDepths(unittest.TestCase):

    def test_list_of_depths_full_btree_height_3(self) -> None:
        bt: BinaryTree = BinaryTree()
        bt.insert(8)
        bt.insert(4)
        bt.insert(10)
        bt.insert(9)
        bt.insert(2)
        bt.insert(6)
        bt.insert(20)
        self.assertEqual(list(bt), [2, 4, 6, 8, 9, 10, 20])
        self.assertEqual(bt.height(), 3)
        expected_result = {
            0: deque([8]),
            1: deque([4, 10]),
            2: deque([2, 6, 9, 20])
        }
        result = list_of_depths(bt)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
