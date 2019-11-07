#!/usr/bin/python3
'''
Module that implements an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''

import unittest

def unique(string):
    '''checks if string input is unique
    Args:
        string (str): string to check
    '''
    return len(set(string)) is len(string)

def unique2(string):
    '''checks if string input is unique
    args:
        string (str): string to check
    '''
    letters = {}
    for letter in string:
        letters[letter] = letters.get(letter, 0) + 1
        if letters.get(letter) is not None and letters[letter] > 1:
                return False
    return True

def unique3(string):
    '''checks if string input is unique, no new data structures
    args:
        string (str): string to check
    '''
    new_string = sorted(string)
    for idx in range(len(new_string) - 1):
        if new_string[idx] == new_string[idx + 1]:
            return False

    return True


class Test(unittest.TestCase):
    def test1(self):
        all_true = ["Nick", "world"]
        all_false = ["eee", "hello"]

        for idx in range(len(all_true)):
            self.assertTrue(unique(all_true[idx]))
            self.assertFalse(unique(all_false[idx]))

    def test2(self):
        all_true = ["Nick", "world", "Sue", "John", "abcdefghijklmnopqrstuvwxyz"]
        all_false = ["eee", "hello", "nicki", "johnny", "suuu"]

        for idx in range(len(all_true)):
            self.assertTrue(unique2(all_true[idx]))
            self.assertFalse(unique2(all_false[idx]))

    def test3(self):
        all_true = ["Nick", "world", "Sue", "John", "abcdefghijklmnopqrstuvwxyz"]
        all_false = ["eee", "hello", "nicki", "johnny", "suuu"]

        for idx in range(len(all_true)):
            self.assertTrue(unique3(all_true[idx]))
            self.assertFalse(unique3(all_false[idx]))

if __name__ == '__main__':
    unittest.main()
