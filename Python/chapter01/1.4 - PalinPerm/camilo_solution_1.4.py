"""
Palindrome Permutation: Given a string, write a function to check if it is a
permutation of a palin­ drome. A palindrome is a word or phrase that is the same
forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""

import unittest


def PalinPerm(str):
    d = {}
    str = str.replace(' ','').lower()#Take out the spaces
    for i in str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    odd_count = 0 # pop ppo opp
    for keys,value in d.items():
        if value % 2 != 0 and odd_count == 0:# Remeber there should only be 1 where key equals when val%2
            odd_count += 1
        elif value % 2 != 0 and odd_count != 0:
            return False
    return True

class Test(unittest.TestCase):
    def test_palin_perm(self):
        self.assertTrue(PalinPerm('taco cat'))
        self.assertFalse(PalinPerm('taco catt'))


if __name__ == '__main__':
    unittest.main()
