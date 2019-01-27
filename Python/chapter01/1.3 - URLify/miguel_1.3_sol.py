"""
Python version 3.7.0
1.3 - URLify
Write a method to replace all spaces in a string with "%20".
The following only applies to C/C++: "You may assume that the string has sufficient
space at the end to hold the additional characters, and that you are given the "true" length of the string"
(Note: If implementing in Java, please use a character array so that you can perform this operation in place)
Since we are using python, no need to use true length.  I will have two functions, one with
true_length and the other without.
"""
import unittest
from typing import List


def urlify(s: str) -> str:
    """
    Given a string, this function will return a new string
    that replaces all of the spaces of the input string with '%20'.
    :param s: the original string to 'urlify'
    :return: string with each space from s replaced with '%20'
    """
    buf = ['\x00'] * (len(s) * 3)
    for i, c in enumerate(s):
        buf[i] = c

    def _challenge(buf: List[str], original_length: int) -> None:
        """
        Your code here. Challenge rules:
        * You can only reference |buf| and |original_length|, not |s|.
        * You can only allocate O(1) additional memory
        * You need to modify |buf| in-place so that the right answer is returned.
        * You cannot modify any part of the wrapper function.
        :param buf: buffer containing characters
        :param original_length: original length of string
        :return: None
        """
        space_count = 0
        for j in range(original_length):
            if buf[j] == ' ':
                space_count += 1

        chars_per_space = 2
        idx = original_length + space_count * chars_per_space
        for i in range(original_length-1, -1, -1):
            if buf[i] == ' ':
                buf[idx-1] = '0'
                buf[idx-2] = '2'
                buf[idx-3] = '%'
                idx -= 3
                continue
            buf[idx-1] = buf[i]
            idx -= 1
    _challenge(buf, len(s))
    return ''.join(buf).rstrip('\x00')


def urlify_no_true_length(s: str) -> str:
    """
    This is the version of urlify without the true_length argument.
    Given a string and it's "true" length, this function will return a new string
    that replaces all of the spaces of the input string with '%20'.
    Note that this will return a different result than the other urlify
    if the other urlify's true length truncates the string with chars left over.
    Precondition(s):
    - length of s <= true_length
    :param s: the original string to 'urlify'
    :return: string with each space from s replaced with '%20'
    """
    output = []
    for c in s:
        if c == ' ':
            output.append("%20")
            continue
        output.append(c)
    return ''.join(output)


class TestUrlifyFunction(unittest.TestCase):
    def test_urlify(self):
        cases = [
            ("Mr John Smith", "Mr%20John%20Smith"),
            ("Miguel Hernandez", "Miguel%20Hernandez"),
            (" Techqueria", "%20Techqueria"),
            ("a b c d e f g h", "a%20b%20c%20d%20e%20f%20g%20h"),
            ("ihavenospaces", "ihavenospaces"),
            ("nospaces", "nospaces"),
            (" ", "%20")
        ]
        for s, expected in cases:
            self.assertEqual(urlify(s), expected, msg=s)

    def test_urlify_no_true_length(self):
        cases = [
            ("Mr John Smith", "Mr%20John%20Smith"),
            ("Miguel Hernandez", "Miguel%20Hernandez"),
            (" Techqueria ", "%20Techqueria%20"),
            ("a b c d e f g h", "a%20b%20c%20d%20e%20f%20g%20h"),
            ("a b c d e f g h ignore this", "a%20b%20c%20d%20e%20f%20g%20h%20ignore%20this"),
            ("ihavenospaces", "ihavenospaces"),
            ("nospacesIgnoreme", "nospacesIgnoreme"),
            (" ", "%20")
        ]
        for s, expected in cases:
            self.assertEqual(urlify_no_true_length(s), expected, msg=s)


if __name__ == '__main__':
    unittest.main()
