"""
Sum Lists: You have two numbers represented by a linked list, where each node
contains a single digit.
The digits are stored in reverse order, such that the 1 's digit is at the head
of the list. Write a function that adds the two numbers and returns the sum as
a linked list.

EXAMPLE
Input:(7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. Output:2 -> 1 -> 9.That is,912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295. Output:9 -> 1 -> 2.Thatis,912.
Hints: #7, #30, #71, #95, #109


USE THIS IF YOUR SUPERDUPER STUCK
https://www.youtube.com/watch?v=dm9drjU-DuM

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


    def sum_forward_backwards(self,llist_B):
        if llist_B.head == None:
            return "llist_B is None"

        sum_list = linklist()
        head_b = llist_B.head
        curr = self.head #List A
        carry = 0
        while curr or head_b:
            if curr == None and head_b == None:
                i,j = 0
            else:
                i = curr.data
                j = head_b.data

            sum_ = i + j + carry
            if sum_ >= 10:

                carry = 1
                r = sum_ % 10
                sum_list.push(r)

            else:
                carry = 0
                sum_list.push(sum_)
            if curr:
                curr = curr.next
            if head_b:
                head_b = head_b.next

        self.head = sum_list.head





link_A = linklist()
link_B = linklist()
link_A.push(7)
link_A.push(1)
link_A.push(6)

link_B.push(5)
link_B.push(9)
link_B.push(2)
link_A.sum_forward_backwards(link_B)
link_A.printList()
