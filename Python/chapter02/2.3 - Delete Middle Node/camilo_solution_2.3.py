"""
Delete Middle Node: Implement an algorithm to delete a node in the middle
(i.e., any node but the first and last node, not necessarily the exact middle)
of a singly linked list, given only access to that node.
EXAMPLE
lnput:the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e- >f
Hints:#72
"""
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
    def Kth_to_Last(self,num):
        counter = 1 # We need to keep track where we are
        curr = self.head
        goal = self.size - num# kth to last element
        while curr is not None:
            if goal == counter:
                return curr.data
            counter+=1
            curr = curr.next
    """
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






llist = linklist()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(6)
llist.printList()
llist.lenght()

llist.Delete_Middle_Node()# 3 should be removed
llist.printList()
llist.lenght()
