#!/usr/bin/python3
'''
Module that Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.) 
'''

import unittest

def URLify(string, char):
    '''
    Function that replace all spaces in a string with '%20'. 
    Args:
        string (str): a string to modify
    '''
    return string[:char + 1].replace(" ", "%20")    

class Test(unittest.TestCase):
    def test1(self):
        input_string = "Mr Johns Smith      "
        char = 13
        output_string = "Mr%20John%20Smith"
       
        self.assertTrue(URLify(input_string, 13), output_string)
 
if __name__ == '__main__':
    unittest.main()
