class stack:
    def __init__(self):
        self.arr = []

    def push(self,item):
        """
        Add an item to the top of the stack.
        """
        self.arr.insert(0,item)

    def pop_():
        """
        Remove the top item from the stack.
        """
        arr = self.arr
        len_ = len(arr)
        return self.arr.pop(arr)


    def peek(self):
        """
        Return the top of the stack.
        """
        return self.arr[0]

    def isEmpty():
        """
        Return true if and only if the stack is empty.
        """
        if self.arr == None:
            return True
        return False



class queue:
    def __init__(self):
        self.arr = []

    def add(self,item):
        """
        Add an item to the end of the list.
        """
        self.arr.append(item)


    def remove(self):
        """
        Remove the first item in the list.
        """
        return self.arr.pop(0)

    def peek(self):
        """
        Return the top of the queue.
        """
        return self.arr[0]

    def isEmpty():
        """
        Return true if and only if the queue is empty.
        """
        if self.arr == None:
            return True
        return False
