"""
Stack Min: How would you design a stack which, in addition to push and pop, has
a function min which returns the minimum element? Push, pop and min should all
operate in 0(1) time.
Hints:#27, #59, #78
"""

import unittest


class stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        """
        Add an item to the top of the stack.
        """
        self.items.append(item)

    def pop_(self):
        """
        Remove the top item from the stack.
        """

        return self.items.pop()


    def peek(self):
        """
        Return the top of the stack.
        """
        return  self.items[len(self.items)-1]

    def isEmpty(self):
        """
        Return true if and only if the stack is empty.
        """
        if self.items == None:
            return True
        return False

    def print_stack(self):
        print(self.items)

    def stackMin(self):
        arr = self.items
        min = arr[0]
        for i in range(len(arr)):
            if min > arr[i]:
                min = arr[i]

        return min


class Test(unittest.TestCase):
    def test_stack_min(self):
        st1 = stack()
        st1.push(7)
        st1.push(4)
        st1.push(5)
        st1.push(9)
        st1.push(0)
        st1.push(6)
        st1.push(1)
        st1.push(5)
        st1.push(7)
        self.assertEqual(st1.stackMin(), 0)

if __name__ == '__main__':
    unittest.main()
