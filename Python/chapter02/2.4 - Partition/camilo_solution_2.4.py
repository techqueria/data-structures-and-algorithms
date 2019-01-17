"""
Partition: Write code to partition a linked list around a value x, such that all
 nodes less than x come before all nodes greater than or equal to x. If x is
 contained within the list, the values of x only need to be after the elements
 less than x (see below). The partition element x can appear anywhere in the
 "right partition"; it does not need to appear between the left and right
 partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] Output: 3 -> 1 -> 2 ->
10 -> 5 -> 5 -> 8
Hints: #3, #24
"""

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

    def partition(self,num):
        #llist_A and llist_b to be continers
        list_A = linklist()
        list_B = linklist()
        curr = self.head
        # Idea: Make two seperate llink and smash them together

        while curr is not None:
            if curr.data <= num:
                list_A.push(curr.data)
            elif curr.data > num:
                list_B.push(curr.data)
            curr = curr.next
        list_A.printList()
        list_B.printList()

        #Go through all of A the point the end of A to the begining of B

        self.head = list_A.head
        head_A = list_A.head
        while head_A.next:
            head_A = head_A.next
        head_A.next = list_B.head

















llist = linklist()
llist.push(3)
llist.push(5)
llist.push(8)
llist.push(5)
llist.push(10)
llist.push(2)
llist.push(1)
llist.printList()
llist.lenght()
llist.partition(5)
llist.printList()
