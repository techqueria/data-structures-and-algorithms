"""
Python version 3.7.0
1.5 - One Away
There are three types of edits that can be performed on strings:  insert a character,
remove a character, or replace a character.  Given two strings, write a function to check
if they are one edit (or zero edits) away.
"""
import unittest
import collections
from typing import Callable


def one_away(s1: str, s2: str) -> bool:
    """
    Checks if two strings are one edit or zero edits away.
    There are 3 types of edits:
    1. insert a character
    2. remove a character
    3. replace a character
    Zero edits away means the two strings are exactly the same.
    We will analyze character frequencies to detect anomalies.
    An anomaly can be any of the 3 types of edits.
    Runtime:  O(n + m), where n is length of s1 and m is length of s2
    Space Complexity:  O(n + m)
    :param s1: one string we want to compare
    :param s2: other string to compare
    :return: true if one or zero edits away, false otherwise
    """
    # if size differs by more than 1, guaranteed more than one anomaly.
    if abs(len(s1) - len(s2)) > 1:
        return False

    char_freqs_s1 = collections.Counter(s1)
    char_freqs_s2 = collections.Counter(s2)

    anomalies = 0
    for key, value in char_freqs_s1.items():
        if key not in char_freqs_s2 or value != char_freqs_s2[key]:
            anomalies += 1
        if anomalies > 1:
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
        ]
        for s1, s2, expected in cases:
            self.assertEqual(f(s1, s2), expected, msg=(s1, s2))

    def test_one_away(self):
        self._run_tests(one_away)


if __name__ == '__main__':
    unittest.main()
