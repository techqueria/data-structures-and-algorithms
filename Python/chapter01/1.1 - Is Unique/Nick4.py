#!/usr/bin/python3
'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words
'''

import unittest


def palperm(string):
    '''
    Function that checks if it is a permutation of a palindrome
    Args:
        string (str): a string to check for all palindrome permutations
    '''
    table = {}
    count = 0
    for letter in string.lower().replace(" ", ""):
        table[letter] = table.get(letter, 0) + 1

    for key in table:
        if count > 1:
            return False
        if table[key] % 2 == 1:
            count += 1
    return True


class Test(unittest.TestCase):
    def test1(self):
        input_string ="Tact Coa"
        input_string2 ="nick"
        input_string3 ="saippuakivikauppias"
        input_string4 = "iasppaukivikauppias"
        self.assertTrue(palperm(input_string))
        self.assertFalse(palperm(input_string2))
        self.assertTrue(palperm(input_string3))
        self.assertTrue(palperm(input_string4))

if __name__ == '__main__':
    unittest.main()
