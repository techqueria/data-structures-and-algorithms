"""Python Version 3.9.2
4.1 - Route Between Nodes:
Given a directed graph, design an algorithm to
find out whether there is a route between two nodes.
"""
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
    visited_nodes: List[Node] = []
    visited_nodes.append(root)
    queue: Deque[Node] = deque()
    root.visited = True
    queue.append(root)
    while queue:
        node = queue.popleft()
        node.visited = True
        # print(f'Visiting node ({node.id})')
        for n in node.children:
            if not n.visited:
                n.visited = True
                queue.append(n)
                visited_nodes.append(n)
    # reset visited state
    g = Graph(visited_nodes)
    g.reset_visited()
    return list(map(lambda n: n.id, visited_nodes))


def route_between_nodes(src: Node, dest: Node) -> bool:
    """This function will return true if a path
    is found between two nodes, false otherwise.
    The idea is to perform a breadth first search
    from src to dest. After obtaining a list of
    nodes visited, we simply check to see if destination
    node id is in there.

    Runtime Complexity:
        O(V + E) where V represents the number of
        nodes in the graph and E represents the number
        of edges in this graph.
    Space Complexity:
        O(V) where V represents the number of existing nodes
        in the graph.

    Args:
        src (Node): from node
        dest (Node): destination node

    Returns:
        bool: whether a path between src and dest exists
    """
    ids_visited: List[int] = bfs_search(src)
    return True if dest.id in ids_visited else False


class TestRouteBetweenNodes(unittest.TestCase):
    def test_route_between_nodes(self):
        n0 = Node(0, [])
        n1 = Node(1, [])
        n2 = Node(2, [])
        n3 = Node(3, [])
        n4 = Node(4, [])
        n5 = Node(5, [])
        n0.add_child(n1, n4, n5)
        n1.add_child(n3, n4)
        n2.add_child(n1)
        n3.add_child(n2, n4)
        # must remember to reset node visited properties
        # before each fresh run
        g = Graph([n0, n1, n2, n3, n4, n5])
        # There is a route from node 0 to node 2
        self.assertTrue(route_between_nodes(n0, n2))
        # No route between node 1 and node 0
        self.assertFalse(route_between_nodes(n1, n0))
        # There is a route from node 2 to node 3
        self.assertTrue(route_between_nodes(n2, n3))

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
        n2.add_child(n1)
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
        n2.add_child(n1)
        n3.add_child(n2, n4)
        result: List[int] = bfs_search(n0)
        self.assertEqual(result, [0, 1, 4, 5, 3, 2])


if __name__ == '__main__':
    unittest.main()
