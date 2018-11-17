#!/usr/bin/python3
'''
Module that Given two strings, write a method to decide if one is a permutation of the
other. 

'''

import unittest

def permutation(string1, string2):
    '''
    Checks two strings if one is a permutation of the other
    Args:
        string1 (str): a string
        string2 (str): another string
    '''
    if len(string1) is not len(string2):
        return False

    n1, n2 = sorted(string1), sorted(string2)
    return n1 == n2 

def permutation2(string1, string2):
    '''
    Checks two strings if one is a permutation of the other
    Args:
        string1 (str): a string
        string2 (str): another string
    '''
    if len(string1) is not len(string2):
        return False

    d1, d2 = {}, {}
    for idx in range(len(string1)):
        d1[string1[idx]] = d1.get(string1[idx], 0) + 1
        d2[string2[idx]] = d2.get(string2[idx], 0) + 1

    return d1 == d2

def permutation3(string1, string2):
    '''
    Checks two strings if one is a permutation of the other
    Args:
        string1 (str): a string
        string2 (str): another string
    '''


class Test(unittest.TestCase):
    def test1(self):
        t1 = "nickiiii"
        t2 = "iiiiinck"
        x1, x2 = "hello", "world"
        self.assertTrue(permutation(t1,t2))
        self.assertFalse(permutation(x1, x2))

    def test2(self):
        self.assertFalse(permutation2("nickjjj", "nickkki"))
        self.assertTrue(permutation2("iiiiinn", "nniiiii"))

    def test3(self):
        pass

if __name__ == '__main__':
    unittest.main()
