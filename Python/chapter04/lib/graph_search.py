import unittest

from collections import deque
from dataclasses import dataclass
from typing import List, Deque, Set


@dataclass
class Graph:
    nodes: 'List[Node]'

    def print_graph(self):
        for node in self.nodes:
            node.print_children()

    def reset_visited(self):
        for node in self.nodes:
            node.visited = False


@dataclass
class Node:
    id: int
    children: 'List[Node]'
    visited: bool = False

    def add_child(self, *nodes: 'Node'):
        for node in nodes:
            self.children.append(node)

    def print_children(self):
        logging.debug('Adjacency list for node %s: %s', self.id, ', '.join(str(child.id) for child in self.children))

    def __str__(self):
        return f'Node ({self.id}), visited: {self.visited}'


def dfs_search(root: Node, visited: Set[int] = set()) -> List[int]:
    """Simple DFS.
    takes in a root, returns a list
    of ids of the sequence of visited
    nodes.

    Args:
        root (Node): starting node

    Returns:
        List[int]: list of node IDs (i.e. [0, 1, 3])
    """
    if root is None:
        raise TypeError
    visited_list: List[int] = [root.id]
    # if already added, won't add to set.
    # line 55 is mainly for initial empty set.
    # future .adds will attempt to add value that
    # already exists in the set.
    # result will be a no-op
    visited.add(root.id)
    # print(f'Visiting node ({root.id})')
    # print(root.children)
    for node in root.children:
        if node.id not in visited:
            visited.add(node.id)
            visited_list.extend(dfs_search(node, visited))
    return visited_list

def bfs_search(root: Node) -> List[int]:
    """Simple BFS.
    takes in a root, returns a list
    of ids of the sequence of visited
    nodes.

    Args:
        root (Node): starting node

    Returns:
        List[int]: List[int]: list of node IDs (i.e. [0, 1, 4])
    """
    visited_list: List[int] = [root.id]
    visited: Set[int] = set([root.id])
    queue: Deque[Node] = deque([root])
    while queue:
        node = queue.popleft()
        # print(f'Visiting node ({node.id})')
        for n in node.children:
            if n.id not in visited:
                queue.append(n)
                visited_list.append(n.id)
                visited.add(n.id)
    return visited_list


class TestMyGraphSearch(unittest.TestCase):

    def test_basic_graph_creation(self):
        n0 = Node(0, [])
        n1 = Node(1, [])
        n2 = Node(2, [])
        n3 = Node(3, [])
        n4 = Node(4, [])
        n5 = Node(5, [])
        n6 = Node(6, [])
        n0.add_child(n1)
        n1.add_child(n2)
        n2.add_child(n0, n3)
        n3.add_child(n2)
        n4.add_child(n6)
        n5.add_child(n4)
        n6.add_child(n5)
        nodes = [n0, n1, n2, n3, n4, n5, n6]
        g = Graph(nodes)
        # g.print_graph()

    def test_basic_depth_first_search(self):
        n0 = Node(0, [])
        n1 = Node(1, [])
        n2 = Node(2, [])
        n3 = Node(3, [])
        n4 = Node(4, [])
        n5 = Node(5, [])
        n0.add_child(n1, n4, n5)
        n1.add_child(n3, n4)
        n3.add_child(n2, n4)
        result: List[int] = dfs_search(n0)
        self.assertEqual(result, [0, 1, 3, 2, 4, 5])

    def test_basic_breadth_first_search(self):
        n0 = Node(0, [])
        n1 = Node(1, [])
        n2 = Node(2, [])
        n3 = Node(3, [])
        n4 = Node(4, [])
        n5 = Node(5, [])
        n0.add_child(n1, n4, n5)
        n1.add_child(n3, n4)
        n3.add_child(n2, n4)
        result: List[int] = bfs_search(n0)
        self.assertEqual(result, [0, 1, 4, 5, 3, 2])


if __name__ == '__main__':
    unittest.main()
