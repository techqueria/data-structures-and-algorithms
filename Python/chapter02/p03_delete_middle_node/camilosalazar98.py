"""
Delete Middle Node: Implement an algorithm to delete a node in the middle
(i.e., any node but the first and last node, not necessarily the exact middle)
of a singly linked list, given only access to that node.
EXAMPLE
lnput:the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e- >f
Hints:#72
"""

import unittest


class Node:
    #Singly link list
    def __init__(self,data):
        self.data = data
        self.next = None

class linklist:
    #linkList class
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,data):
        node = Node(data)# create a new node

        if self.head == None: #check to see if the head node is empty
            self.head = node # If its empty add it to the new node
            self.size = 1
            return
        #if the head of the linklist is filled

        current = self.head
        while current.next is not None:#Check the current postion is empty
        #Move to the next line if nothing is there
            current = current.next


        current.next = node #point self.head to a new node
        self.size+=1

    def length(self):
        #note the count doesn't start at zero
        cur = self.head
        counter = 0
        while cur is not None:
            counter+=1
            cur = cur.next
        return counter

    def toList(self):
        curr = self.head
        elem = []

        while(curr != None):
            elem.append(curr.data)
            curr = curr.next
        return elem

    #1->2->3
    def remove_node(self,data):
        #1->2->3
        curr = self.head
        if curr is not None and curr.data == data:
            self.head = curr.next
            curr = None
        #look for the node that has the data we are looking for
        while curr is not None:
            if curr.data == data:
                break
            prev = curr
            curr = curr.next

        #if data isn't found just reutrn
        if(curr == None):
            return

        #allow us to unlink the nodes
        prev.next = curr.next
        curr = None

    def Delete_Middle_Node(self):
        counter = 1
        curr = self.head
        goal = (self.size//2)# floor division
        while curr is not None:
            if counter == goal:
                self.remove_node(curr.data)
                return
            counter+=1
            curr = curr.next


class Test(unittest.TestCase):
    def test_delete_middle_node(self):
        llist = linklist()
        llist.push(1)
        llist.push(2)
        llist.push(3)
        llist.push(4)
        llist.push(5)
        llist.push(6)
        self.assertEqual(llist.toList(), [1, 2, 3, 4, 5, 6])
        self.assertEqual(llist.length(), 6)

        llist.Delete_Middle_Node()
        self.assertEqual(llist.toList(), [1, 2, 4, 5, 6])
        self.assertEqual(llist.length(), 5)


if __name__ == '__main__':
    unittest.main()
