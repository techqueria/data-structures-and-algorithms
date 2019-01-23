"""
Python version 3.7.0
1.2 - Check Permutation
Given two strings, write a method to decide if one is a permutation of the other.
"""
import unittest
from typing import Callable


def check_permutation(s1: str, s2: str) -> bool:
    """
    Determines if a s1 is a permutation of s2.
    s1 is a permutation of s2 if the characters from s1 map to
    the same characters in s2 in a one-to-one correspondence AND s1 and s2 are of the same length.
    Runtime:  O(n + m), where n is the length of s1 and m is the length of s2.
    Given:		            Expect:
    "tacos", "costa"            True
    "tacoos", "costa"           False
    "swag", "hello"         False
    "hi", "hello"           False
    "hola", "loha"          True
    "p3nding", "dingp3n"            True
    "", "test"          False
    "", ""          True
    "test2", ""         False
    :param s1: string of size n
    :param s2: string of size m
    :return: True if s1 is a permutation of s2, False otherwise
    """
    # permutations must be of equal length, one-to-one
    if len(s1) != len(s2):
        return False
    freqs_s1 = {}
    # build histogram of seen characters in s1
    # using histogram because string could have repeated characters
    for c in s1:
        if c not in freqs_s1:
            freqs_s1[c] = 1
            continue
        freqs_s1[c] += 1

    freqs_s2 = {}
    for c in s2:
        # if character in s2 not in s1, then this is not a permutation
        if c not in freqs_s1:
            return False
        # otherwise, populate as normal
        if c not in freqs_s2:
            freqs_s2[c] = 1
            continue
        freqs_s2[c] += 1

    # compare frequences of characters for s1 and s2
    for key, val in freqs_s1.items():
        if val != freqs_s2[key]:
            # character counts between s1 and s2 don't match
            return False
    return True


class TestCheckPermutationFunction(unittest.TestCase):
    def _run_tests(self, f: Callable[[str, str], None]) -> None:
        false_cases = [
            ("tacoos", "costa"), ("swag", "hello"), ("hi", "hello"), ("tacooos", "costaaa"),
            ("", "test"), ("test2", "")
        ]
        for case in false_cases:
            self.assertFalse(f(case[0], case[1]), msg=case)

        true_cases = [
            ("tacos", "costa"), ("hola", "loha"), ("p3nding", "dingp3n"), ("same", "same"), ("", "")
        ]
        for case in true_cases:
            self.assertTrue(f(case[0], case[1]), msg=case)
        with self.assertRaises(TypeError):
            f(8)

    def test_check_permutation(self):
        self._run_tests(check_permutation)


if __name__ == '__main__':
    unittest.main()
