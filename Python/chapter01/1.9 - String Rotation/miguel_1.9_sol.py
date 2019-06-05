"""
Python version 3.7.0
1.9 - String Rotation
Assume you have a method isSubstring which
checks if one word is a substring
of another.  Given two strings, s1 and s2,
write code to check if s2 is a
rotation of s1 using only one call to isSubstring
(e.g. 'waterbottle' is a rotation of 'erbottlewat')
"""
import unittest


def is_substring(sub: str, s: str) -> bool:
    """
    is_substring checks if 'sub' is a substring of 's'
    :param sub: the substring
    :param s: the alleged full string
    :return: true if sub is a substring of s, false otherwise
    """
    return sub in s


def string_rotation(s1: str, s2: str) -> bool:
    """
    Given two strings, string_rotation will check if s2 is a rotation of s1
    using only one call to isSubstring.
    We will loop through the original string and compare chars of
    rotated string.  At the first character equality, we will
    compare the rest of the original string to the rotated
    string's substring of the same length.
    If they match, then we save the index of the
    rotated string + 1, and if whatever is left of
    s1 is a substring of s2, then we must have a
    rotation since we compared the complementary part already.
    Runtime: Worst case:  O(n^2)
    Space Complexity:  O(1)
    :param s1: the rotated string
    :param s2: the original string
    :return: true if s2 is a rotation of s1, false otherwise
    """
    # not rotation if lengths don't match
    if len(s1) != len(s2):
        return False
    # if they match, but both empty, return true
    if s1 == '' and s2 == '':
        return True
    size = len(s1)
    start_idx = -1
    for i, c in enumerate(s2):
        if c != s1[0]:
            continue
        # check if substring in s2 from i to the end
        # matches s1 from beginning to remaining length of s2
        if s2[i:] == s1[0:size - i]:
            # store starting idx of remaining substring in s2
            start_idx = size - i
            break
    if start_idx == -1:
        return False
    if is_substring(s1[start_idx:], s2):
        return True
    return False


class TestStringRotation(unittest.TestCase):

    def setUp(self):
        self.str_rotation_cases = [
            ('erbottlewat', 'waterbottle', True),
            ('erbottlewet', 'weterbottle', True),
            ('same', 'same', True),
            ('oneoff', 'oneof', False),
            ('erbottleabc', 'waterbottle', False),
            ('ion?rotat', 'rotation?', True),
            ('', '', True),
            ('a', 'a', True),
            ('a', 'b', False),
            ('erbottlewat', 'eeeeeeeeee', False)
        ]

        self.is_substring_cases = [
            ('swag', 'swagger', True),
            ('swagger', 'swag', False),
            ('test', 'testing', True),
            ('', 'sdfkjslf', True),
            ('abcd', 'defg', False)
        ]

    def test_is_substring(self):
        for sub, s, expected in self.is_substring_cases:
            self.assertEqual(is_substring(sub, s), expected, msg=(sub, s, expected))

    def test_string_rotation(self):
        for s1, s2, expected in self.str_rotation_cases:
            self.assertEqual(string_rotation(s1, s2), expected, msg=(s1, s2, expected))


if __name__ == '__main__':
    unittest.main()
