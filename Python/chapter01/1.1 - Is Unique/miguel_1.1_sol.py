"""
Python version 3.7.0
1.1
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
What if the input string is empty?
I assume that the user will input a non-empty string
If the string is empty, then raise a ValueError exception
If the input is NOT a string, then raise a TypeError exception
"""
import unittest
from typing import Callable


def is_unique(input_str: str) -> bool:
    """
    Determines if input_str has all unique characters.
    For all characters in the input_str with n >= 1, where n is the number of characters in input_str,
    there must be no duplicate characters.
    In the worst case, the run time of this function will be O(n)
    Space complexity will be O(n)
    Given:		Expect:
    tacos		True
    swag		True
    bobby		False
    california	False
    orbit       True
    e       True
    ""      True
    :param input_str: the string we want to check characters of
    :return: returns True if input_str has all unique characters, False otherwise
    """
    chars_seen = set()
    for c in input_str:
        if c in chars_seen:
            return False
        chars_seen.add(c)
    return True


def is_unique_no_additional_data_structures(input_str: str) -> bool:
    """
    Variant of is_unique.  Uses no additional data structures (besides the variables from the iterator)
    However, the drawback is that the runtime is O((n*n-1)/2) = O(n^2), where n is the number of characters
    in the input_str.
    Given:		Expect:
    tacos		True
    swag		True
    bobby		False
    california	False
    orbit       True
    e       True
    ""      True
    :param input_str: the string we want to check characters of
    :return: returns True if input_str has all unique characters, False otherwise
    """
    for i, c in enumerate(input_str):
        if c in input_str[i+1:]:
            return False
    return True


class TestIsUniqueFunction(unittest.TestCase):
    def _run_tests(self, f: Callable[[str], None]) -> None:
        for case in ["techqueria", "bobby", "california"]:
            self.assertFalse(f(case), msg=case)
        for case in ["tacos", "swag", "orbit", "e", ""]:
            self.assertTrue(f(case), msg=case)
        with self.assertRaises(TypeError):
            f(8)

    def test_is_unique(self):
        self._run_tests(is_unique)

    def test_is_unique_no_additional_data_structures(self):
        self._run_tests(is_unique_no_additional_data_structures)


if __name__ == '__main__':
    unittest.main()
