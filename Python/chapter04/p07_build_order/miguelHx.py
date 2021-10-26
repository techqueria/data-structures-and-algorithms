"""Python Version 3.9.2
4.7 - Build Order:
You are given a list of projects and a list of dependencies
(which is a list of pairs of projects, where the second project is dependent on the first project).
All of a project's dependencies must be built before the project is.
Find a build order that will allow the projects to be built. If there is no
valid build order, return an error.
EXAMPLE
Input:
    projects:  a, b, c, d, e, f
    dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output:
    f, e, a, b, d, c
"""
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


@dataclass
class Node:
    id: int
    children: 'List[Node]'

    def add_child(self, *nodes: 'Node'):
        for node in nodes:
            self.children.append(node)

    def children_as_str(self) -> str:
        return ', '.join(str(child.id) for child in self.children)

    def print_children(self):
        logging.debug('Adjacency list for node %s: %s', self.id, self.children_as_str())

    def __str__(self):
        return f'Node ({self.id}), children: {self.children_as_str()}'

def bfs_search_exhaustive(root: Node) -> List[int]:
    """Simple BFS.
    takes in a root, returns a list
    of ids of the sequence of visited
    nodes. Goes through entire graph.
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


def bfs_search_for_dest(root: Node, dest: Node) -> List[int]:
    """Simple BFS.
    takes in a root, returns a list
    of ids of the sequence of visited
    nodes. Stops at destination node
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
            if n.id == dest.id:
                # done searching
                return visited_list
    return visited_list

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
    ids_visited: List[int] = bfs_search_for_dest(src, dest)
    return dest.id in ids_visited


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

    def test_basic_breadth_first_search_exhaustive(self):
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
        result: List[int] = bfs_search_exhaustive(n0)
        self.assertEqual(result, [0, 1, 4, 5, 3, 2])


if __name__ == '__main__':
    unittest.main()
