"""
Intersection: Given two (singly) linked lists, determine if the two lists
intersect. Return the inter­secting node. Note that the intersection is defined
based on reference, not value.That is, if the kth node of the first linked list
is the exact same node (by reference) as the jth node of the second linked list,
then they are intersecting.
Hints:#20, #45, #55, #65, #76, #93, #111, #120, #129


Had a really hard time with this question:
https://www.youtube.com/watch?v=gMeDsyEXnbM

"""

import unittest

class Node:
    #Singly link list
    def __init__(self,data = None):
        self.data = data
        self.next = None

class linklist:
    #linkList class
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

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

    def lenght(self):
        #note the count doesn't start at zero
        cur = self.head
        counter = 0
        while cur is not None:
            counter+=1
            cur = cur.next
        print('Linklist len: '+str(counter))
        return counter

    def printList(self):
        curr = self.head
        elem = []

        while(curr != None):
            elem.append(curr.data)
            curr = curr.next
        print(elem)
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

    """
    def make_next(self,llist,num):
        curr_llist = llist.head
        curr = self.head

        size_ = self.size - llist.size
        print(size_)
        size = 0
        if self.size == llist.size:
            while curr and curr_llist is not None:
                if curr.data == num:
                    curr_llist.next = curr

                curr = curr.next
                curr_llist = curr_llist.next

        while curr is not None:
            if size != size_:
                size += 1
                curr = curr.next
            while curr and curr_llist is not None:
                if curr.data == num:
                    curr_llist.next = curr

                curr = curr.next
                curr_llist = curr_llist.next

        self.head = list_A.head
        head_A = list_A.head
        while head_A.next:
            head_A = head_A.next
        head_A.next = list_B.head

    def CombineLlist(self,list_A,list_B):
        list_B = list_B.head
        head_A = self.head
        while head_A is not None:
            head_A = head_A.next
        head_A.next = list_B.head
"""


def intersection(listA,ListB):
    headA = listA.head
    headB = ListB.head

    if not headA or not headB:
        return None

    a = headA
    b = headB


    while a != b and a!= None and b != None:
        if not a:
            a = headB
        else:

            a = a.next

        if not b:
            b = headA
        else:

            b = b.next
    return a.data






# 1->2->3->4->5->6->7
# 3->5->6->7
class Test(unittest.TestCase):
    def setUp(self):
        self.llist_1 = linklist()
        self.llist_2 = linklist()
        self.llist_1.push(1)
        self.llist_1.push(3)
        self.llist_1.push(5)
        self.llist_1.push(7)
        self.llist_1.push(9)
        self.llist_1.push(11)
        self.llist_2.push(2)
        self.llist_2.push(4)
        self.llist_2.push(9)
        self.llist_2.push(11)

    def test_intersection(self):
        self.assertEqual(intersection(self.llist_1, self.llist_2), 9)


if __name__ == '__main__':
    unittest.main()
