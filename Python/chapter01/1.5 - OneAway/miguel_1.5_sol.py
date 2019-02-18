"""
Python version 3.7.0
1.5 - One Away
There are three types of edits that can be performed on strings:  insert a character,
remove a character, or replace a character.  Given two strings, write a function to check
if they are one edit (or zero edits) away.
"""
import unittest
from typing import Callable


def one_away(s1: str, s2: str) -> bool:
    """
    Checks if two strings are one edit or zero edits away.
    There are 3 types of edits:
    1. insert a character
    2. remove a character
    3. replace a character
    Zero edits away means the two strings are exactly the same.
    We will do different checks depending on the size different of the strings.
    Runtime:  O(n), where n is length of s1
    Space Complexity:  O(n + n +/- 1) = O(n), where n is length of s1
    :param s1: one string we want to compare
    :param s2: other string to compare
    :return: true if one or zero edits away, false otherwise
    """
    # if size differs by more than 1, guaranteed more than one edit distance.
    if abs(len(s1) - len(s2)) > 1:
        return False
    # if size is the same, scan for edits
    if len(s1) == len(s2):
        edits = 0
        for i, c in enumerate(s1):
            if c == s2[i]:
                continue
            edits += 1
            if edits > 1:
                return False
        return True
    # otherwise, we have an insertion/deletion
    # compare both strings for insertion/deletion
    # want to loop through the shorter string to avoid going out of bounds
    s_short = s1 if len(s1) < len(s2) else s2
    s_long = s1 if len(s1) > len(s2) else s2

    addend = 0
    for i, c in enumerate(s_short):
        if c == s_long[i + addend]:
            continue
        if i == i + addend:
            # addend is 0, will check next char in next iteration
            addend += 1
            continue
        # otherwise, addend is not 0, and we did not match characters.
        # guaranteed at least 2 edit distance
        return False
    return True


class TestOneAwayFunction(unittest.TestCase):
    def _run_tests(self, f: Callable[[str, str], bool]) -> None:
        cases = [
            ("pale", "ple", True),
            ("pales", "pale", True),
            ("pale", "bale", True),
            ("pale", "bake", False),
            ("", "swag", False),
            ("paale", "pale", True),
            ("a", "", True),
            ("", "b", True),
            ("a", "b", True),
            ("", "", True),
            ("pale", "elap", False),
            ("pale", "elaps", False),
            ("pale", "palse", True)
        ]
        for s1, s2, expected in cases:
            self.assertEqual(f(s1, s2), expected, msg=(s1, s2))

    def test_one_away(self):
        self._run_tests(one_away)


if __name__ == '__main__':
    unittest.main()
