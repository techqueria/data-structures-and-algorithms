"""
Python version 3.7.0
1.3 - URLify
Write a method to replace all spaces in a string with "%20".  You may assume that the string has sufficient
space at the end to hold the additional characters, and that you are given the "true" length of the string.
(Note: If implementing in Java, please use a character array so that you can perform this operation in place)
"""
import unittest
from typing import Callable


def urlify(s: str, true_length: int) -> str:
    """
    Given a string and it's "true" length, this function will return a new string
    that replaces all of the spaces of the input string with '%20'.
    Precondition(s):
    - length of s <= true_length
    :param s: the original string to 'urlify'
    :param true_length: since s may have additional characters, we focus on true_length instead of actual s length
    :return: string with each space from s replaced with '%20'
    """
    output = ""
    for i, c in enumerate(s):
        if i == true_length:
            break
        if c == ' ':
            output += "%20"
            continue
        output += c
    return output


class TestUrlifyFunction(unittest.TestCase):
    def _run_tests(self, f: Callable[[str, int], str]) -> None:
        cases = [
            (("Mr John Smith     ", 13), "Mr%20John%20Smith"),
            (("Miguel Hernandez", 16), "Miguel%20Hernandez"),
            ((" Techqueria ", 11), "%20Techqueria"),
            (("a b c d e f g h", 15), "a%20b%20c%20d%20e%20f%20g%20h"),
            (("a b c d e f g h ignore this", 15), "a%20b%20c%20d%20e%20f%20g%20h"),
            (("ihavenospaces", 13), "ihavenospaces"),
            (("nospacesIgnoreme", 8), "nospaces")
        ]
        for args, expected in cases:
            self.assertEqual(f(*args), expected, msg=args)

    def test_urlify(self):
        self._run_tests(urlify)


if __name__ == '__main__':
    unittest.main()
