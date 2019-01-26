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
    # Below link goes over string concat efficiency in python (I will use method 4
    # https://waymoot.org/home/python_string/
    output = []
    for c in s[0:true_length]:
        if c == ' ':
            output.append("%20")
            continue
        output.append(c)
    return ''.join(output)


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
    def _run_tests(self, f1: Callable[[str, int], str], f2: Callable[[str], str]) -> None:
        cases = [
            (("Mr John Smith     ", 13), "Mr%20John%20Smith"),
            (("Miguel Hernandez", 16), "Miguel%20Hernandez"),
            ((" Techqueria ", 11), "%20Techqueria"),
            (("a b c d e f g h", 15), "a%20b%20c%20d%20e%20f%20g%20h"),
            (("a b c d e f g h ignore this", 15), "a%20b%20c%20d%20e%20f%20g%20h"),
            (("ihavenospaces", 13), "ihavenospaces"),
            (("nospacesIgnoreme", 8), "nospaces")
        ]
        cases_no_true_length = [
            ("Mr John Smith", "Mr%20John%20Smith"),
            ("Miguel Hernandez", "Miguel%20Hernandez"),
            (" Techqueria ", "%20Techqueria%20"),
            ("a b c d e f g h", "a%20b%20c%20d%20e%20f%20g%20h"),
            ("a b c d e f g h ignore this", "a%20b%20c%20d%20e%20f%20g%20h%20ignore%20this"),
            ("ihavenospaces", "ihavenospaces"),
            ("nospacesIgnoreme", "nospacesIgnoreme")
        ]
        for args, expected in cases:
            self.assertEqual(f1(*args), expected, msg=args)
        for s, expected in cases_no_true_length:
            self.assertEqual(f2(s), expected, msg=s)

    def test_urlify(self):
        self._run_tests(urlify, urlify_no_true_length)


if __name__ == '__main__':
    unittest.main()
