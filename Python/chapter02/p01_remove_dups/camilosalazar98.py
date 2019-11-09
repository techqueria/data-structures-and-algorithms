"""Romove Dups! Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary
buffer is not allowed? Hints: #9, #40
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

    def push(self,data):
        node = Node(data)# create a new node

        if self.head == None: #check to see if the head node is empty
            self.head = node # If its empty add it to the new node
            return
        #if the head of the linklist is filled

        current = self.head
        while current.next is not None:#Check the current postion is empty
        #Move to the next line if nothing is there
            current = current.next

        current.next = node #point self.head to a new node

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

    def remove_dups(self):
        d_ = set()# create a set where only unquine element can be in
        curr = self.head
        while curr is not None:
            d_.add(curr.data)#add all the elements to the set
            curr = curr.next
        d_ = list(d_)#make theem in to a list
        self.head = None#clear the orignal link list
        for i in range(len(d_)):
            self.push(d_[i])#Use the element in the set a build a linklist with no dups






class Test(unittest.TestCase):
    def test_remove_dups(self):
        llist = linklist()
        llist.push(2)
        llist.push(2)
        llist.push(2)
        llist.push(2)
        llist.push(2)
        self.assertEqual(llist.toList(), [2, 2, 2, 2, 2])
        self.assertEqual(llist.length(), 5)
        #Testing 1->2->1->3->1 result should only be 1->2->3
        llist.remove_dups()
        self.assertEqual(llist.toList(), [2])
        self.assertEqual(llist.length(), 1)


if __name__ =='__main__':
    unittest.main()
