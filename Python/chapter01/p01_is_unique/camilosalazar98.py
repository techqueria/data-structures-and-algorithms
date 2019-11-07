"""
Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""

import unittest

#This soluation is O(n^2)

def isUnique(string_):
    for i in range(len(string_)):
        i = 0
        for j in range(1,len(string_)):
            if string_[i] == string_[j]:
                return False
    return True


#let's see if we can go faster

def isUnique_(string_):
    d = {}
    for i in string_:
        if i in d:
            d[i] += 1

        else:
            d[i] = 1
    for keys,value in d.items():
        if value > 1:
            return False
    return True


class Test(unittest.TestCase):
    def test_quadradic(self):
        self.assertFalse(isUnique("GeeksforGeeks"))

    def test_linear(self):
        self.assertTrue(isUnique_("camilo"))


if __name__ == '__main__':
    unittest.main()
