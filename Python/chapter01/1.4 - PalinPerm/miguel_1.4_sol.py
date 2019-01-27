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


def is_permutation_of_palindrome(word: str) -> bool:
    """
    Checks if a word is a palindrome by analyzing the frequencies of characters.
    A palindrome is a word or phrase that is the same forwards and backwards.
    When determining character frequencies, word will be put to lowercase
    and spaces will not be counted
    A palindrome also has the following property:
    * all characters have an even count or all except one are even
    Runtime: O(n)
    Space Complexity: O(n)
    :param word: the word we check, 'word' is a possible permutation of a palindrome
    :return: true if word is a permutation of a palindrome, false otherwise
    """
    char_frequencies = collections.Counter(word.lower().replace(' ', ''))
    num_odd_freq_chars = 0
    num_even_freq_chars = 0

    for key, val in char_frequencies.items():
        if num_odd_freq_chars > 1:
            return False
        if val % 2 == 0:
            num_even_freq_chars += 1
        else:
            num_odd_freq_chars += 1
    return True


def _is_palindrome(word: str) -> bool:
    """
    Checks if word is a palindrome by checking if the forward version is the same as the backward version.
    A palindrome is a word or phrase that is the same forwards and backwards.
    Whitespace will not be considered when determining palindrome.
    This function is case insensitive.
    :param word: the word we check, possible permutation of a palindrome
    :return: true if word is a palindrome, false otherwise
    """
    word_no_spaces = word.replace(' ', '').lower()
    reversed_word = word_no_spaces[::-1]
    return word_no_spaces == reversed_word


def is_permutation_of_palindrome_brute_force(word: str) -> bool:
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

    :param word: the string that we want to check for perm of a palindrome
    :return: True if word is a palindrome, False otherwise.
    """
    word_no_spaces = word.replace(' ', '')
    perms = [''.join(p) for p in it.permutations(word_no_spaces)]
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
        for word, expected in cases:
            self.assertEqual(f(word), expected, msg=word)

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
        for word, expected in cases:
            self.assertEqual(_is_palindrome(word), expected, msg=word)


if __name__ == '__main__':
    unittest.main()
