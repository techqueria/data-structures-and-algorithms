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
from typing import List, Deque, Set, Tuple, Dict


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
        print('Adjacency list for node {}: {}'.format(self.id, self.children_as_str()))

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


@dataclass
class DependencyNode:
    id: str
    children: 'List[DependencyNode]'

    def add_child(self, *nodes: 'DependencyNode'):
        for node in nodes:
            self.children.append(node)

    def children_as_str(self) -> str:
        return ', '.join(str(child.id) for child in self.children)

    def print_children(self):
        print('Adjacency list for node {}: {}'.format(self.id, self.children_as_str()))

    def __str__(self):
        return f'Node ({self.id}), children: {self.children_as_str()}'

@dataclass
class DependencyGraph:
    nodes: 'List[DependencyNode]'

    def print_graph(self):
        for node in self.nodes:
            node.print_children()


def build_order(projects: List[str], dependencies: List[Tuple[str, str]]) -> List[str]:
    """Given a list of projects and dependencies,
    this function will find a build order that will
    allow the projects to be build given the dependencies.
    If there is no valid build order, an error will be raised.
    All of a project's dependencies must be built before the project
    is.

    EXAMPLE
    Input:
        projects:  a, b, c, d, e, f
        dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
    Output:
        f, e, a, b, d, c

    Args:
        projects (List[str]): a list of projects
        dependencies (List[Tuple[str, str]]):
            a list of pairs of dependencies (2nd project is dependent on 1st)

    Returns:
        List[str]: a valid build order
    """
    # 0. define output
    output: List[str] = []
    # 1. build a dependency graph
    project_to_node_map: Dict[str, DependencyNode] = {}
    for p in projects:
        project_to_node_map[p] = DependencyNode(p, [])
    for d in dependencies:
        p1 = d[0]
        p2 = d[1]
        project_to_node_map[p2].add_child(project_to_node_map[p1])
    nodes = []
    for node in project_to_node_map.values():
        nodes.append(node)
    # g = DependencyGraph(nodes)
    # print("BUILT GRAPH, HERE IS RESULT:")
    # g.print_graph()

    # 2. define set to keep track of what we already built
    projects_built: Set[str] = set()
    # 3. for each project node, perform a depth-first search
    for project_node in project_to_node_map.values():
        # 4. perform a depth first search
        visited = set()
        stack = []
        stack.append(project_node)
        not_built = []
        while stack:
            node = stack.pop()
            if node.id not in visited:
                visited.add(node.id)
            # get adjacent vertices of popped node.
            # if it has not been visited, push it to stack
            for n in node.children:
                if n.id not in visited and n.id not in projects_built:
                    stack.append(n)
            # check if all children are built.
            all_adjacent_built = True
            for n in node.children:
                if n.id not in projects_built:
                    all_adjacent_built = False
            # if all adjacent nodes are built,
            # then this node can be safely built.
            if all_adjacent_built and node.id not in projects_built:
                projects_built.add(node.id)
                output.append(node.id)
            else:
                not_built.append(node)
        # after traversing, we may have built all children.
        # check nodes that haven't been built from this traversal.
        for node in not_built:
            all_adjacent_built = True
            for n in node.children:
                if n.id not in projects_built:
                    all_adjacent_built = False
            if all_adjacent_built and node.id not in projects_built:
                projects_built.add(node.id)
                output.append(node.id)
    return output

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


class TestBuildOrder(unittest.TestCase):
    def test_build_order_ctci_example(self) -> None:
        projects = ['a', 'b', 'c', 'd', 'e', 'f']
        dependencies = [
            ('a', 'd'),
            ('f', 'b'),
            ('b', 'd'),
            ('f', 'a'),
            ('d', 'c')
        ]
        result = build_order(projects, dependencies)
        # this is the textbook answer, but it is possible to get a
        # different valid build order (depends on algorithm)
        # self.assertEqual(result, ['f', 'e', 'a', 'b', 'd', 'c'])
        self.assertEqual(result, ['f', 'a', 'b', 'd', 'c', 'e'])


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
