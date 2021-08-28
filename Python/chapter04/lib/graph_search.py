import unittest

from collections import deque
from dataclasses import dataclass
from typing import List, Deque


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
        message = f'Adjacency list for node ({self.id}): '
        for child in self.children:
            message += '{}, '.format(child.id)
        print(message)

    def __str__(self):
        return f'Node ({self.id}), visited: {self.visited}'


def dfs_search(root: Node) -> List[int]:
    """Simple DFS.
    takes in a root, returns a list
    of ids of the sequence of visited
    nodes.

    Args:
        root (Node): starting node

    Returns:
        List[int]: list of node IDs (i.e. [0, 1, 3])
    """
    output = []
    if root is None:
        return
    # print(f'Visiting node ({root.id})')
    root.visited = True
    # print(root.children)
    output.append(root.id)
    for node in root.children:
        if not node.visited:
            output.extend(dfs_search(node))
    return output

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
    output = []
    output.append(root.id)
    queue: Deque[Node] = deque()
    root.visited = True
    queue.append(root)
    while len(queue) >= 1:
        node = queue.popleft()
        node.visited = True
        # print(f'Visiting node ({node.id})')
        for n in node.children:
            if not n.visited:
                n.visited = True
                queue.append(n)
                output.append(n.id)
    return output


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
