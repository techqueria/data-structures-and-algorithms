"""
Python version 3.7.0
1.4 - Palindrome Permutation
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.  A permutation is a
rearrangement of letters.  The palindrome does not need to be limited to just dictionary words.
"""
import unittest
import itertools as it
import collections
from typing import Callable


def is_permutation_of_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome by analyzing the frequencies of characters.
    A palindrome is a word or phrase that is the same forwards and backwards.
    When determining character frequencies, word will be put to lowercase
    and spaces will not be counted
    A palindrome also has the following property:
    * at most one character appears an odd number of times
    Runtime: O(n)
    Space Complexity: O(n)
    :param s: the string we check, 's' is a possible permutation of a palindrome
    :return: true if s is a permutation of a palindrome, false otherwise
    """
    char_frequencies = collections.Counter(s.lower().replace(' ', ''))
    num_odd_freq_chars = 0

    for key, val in char_frequencies.items():
        if num_odd_freq_chars > 1:
            return False
        if val % 2 != 0:
            num_odd_freq_chars += 1
    return True


def _is_palindrome(s: str) -> bool:
    """
    Checks if s is a palindrome by checking if the forward version is the same as the backward version.
    A palindrome is a word or phrase that is the same forwards and backwards.
    Whitespace will not be considered when determining palindrome.
    This function is case insensitive.
    :param s: the string we check, possible permutation of a palindrome
    :return: true if s is a palindrome, false otherwise
    """
    s_no_spaces = s.replace(' ', '').lower()
    reversed_s = s_no_spaces[::-1]
    return s_no_spaces == reversed_s


def is_permutation_of_palindrome_brute_force(s: str) -> bool:
    """
    Given a string, this function will return whether the string is a permutation of a palindrome.
    A palindrome is a word or phrase that is the same forwards and backwards.
    A permutation is a rearrangement of letters.
    When evaluating whether a string is the same forwards and backwards, we will
    omit whitespace.  For ex: "taco cat" would not equal "tac ocat" IF we expect a space at the 4th index for
    the reversed version.  So, the space will not be taken into account only when determining palindrome.
    Assuming ASCII
    Runtime is O(n!)
    Space complexity is O(n!)
    Given:      Expect:
    Tact Coa        True (permutations: "taco cat", "atco cta")
    :param s: the string that we want to check for perm of a palindrome
    :return: True if s is a palindrome, False otherwise.
    """
    s_no_spaces = s.replace(' ', '')
    perms = [''.join(p) for p in it.permutations(s_no_spaces)]
    for p in perms:
        if _is_palindrome(p):
            return True
    return False


class TestIsPermutationOfPalindromeFunction(unittest.TestCase):
    def _run_tests(self, f: Callable[[str], bool]) -> None:
        cases = [
            ("Tact Coa", True),
            ("car race", True),
            ("ppilffli", True),
            ("gwas", False),
            ("sldkjflks", False),
            (" ", True),
            ("", True),
            ("a", True)
        ]
        for s, expected in cases:
            self.assertEqual(f(s), expected, msg=s)

    def test_is_permutation_of_palindrome(self):
        self._run_tests(is_permutation_of_palindrome_brute_force)
        self._run_tests(is_permutation_of_palindrome)

    def test_is_palindrome(self):
        cases = [
            ("Taco Cat", True),
            ("race car", True),
            ("flippilf", True),
            ("swag", False),
            ("miguel", False),
            (" ", True),
            ("", True),
            ("a", True),
            ("Tacoo Cat", True),
            ("Tacooo Cat", True)
        ]
        for s, expected in cases:
            self.assertEqual(_is_palindrome(s), expected, msg=s)


if __name__ == '__main__':
    unittest.main()
