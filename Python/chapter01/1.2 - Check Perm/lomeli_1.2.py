# Given two strings, write a method to decide if one is a permutation of the other

import unittest

def isPermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    sort1 = sorted(str1)
    sort2 = sorted(str2)

    return sort1 == sort2


class Test(unittest.TestCase):
    def test_perm_check(self):
        self.assertTrue(isPermutation("stop", "pots"))
        self.assertFalse(isPermutation("stops", "ponds"))


if __name__ == '__main__':
    unittest.main()
