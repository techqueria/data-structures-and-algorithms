#!/usr/bin/python3
import unittest

def is_rotation(s1, s2):
    '''Assumeyou have a method isSubstringwhich checks if oneword is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat"). '''
    if len(s1) is len(s2) and len(s1) > 0:
        return s2 in s1 + s1
    return False


class Test(unittest.TestCase):
    def test1(self):
        self.assertTrue(is_rotation('waterbottle', 'erbottlewat'))
        self.assertFalse(is_rotation('watermellon', 'watermellons'))
        self.assertFalse(is_rotation('waterbottle', 'bottleaterw'))


if __name__ == '__main__':
    unittest.main()
