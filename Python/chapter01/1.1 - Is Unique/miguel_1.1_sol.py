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


def check_is_unique_input(input_str):
    """
    Does some input checking for the is_unique function and its variants
    Raises exceptions if input_str is empty or if input_str is not of type string
    :param input_str: a string that we are checking to make
    :return:
    """
    if not isinstance(input_str, str):
        raise TypeError("expected string as input")
    if input_str == "":
        raise ValueError("empty input string")


def is_unique(input_str):
    """
    Determines if input_str has all unique characters.
    input string MUST have at least 1 character. n>=1, where n is the number of characters in a string.
    Hence, the domain is now defined. Any input not within the domain will not be considered. (n < 1)
    An exception will be raised to handle faulty input.
    Given:		Expect:
    tacos		True
    swag		True
    bobby		False
    california	False
    orbit       True
    e       true
    :param input_str: the string we want to check characters of
    :return: returns True if input_str has all unique characters, False otherwise
    """
    check_is_unique_input(input_str)
    chars_seen = set()
    for c in input_str:
        if c in chars_seen:
            return False
        chars_seen.add(c)
    return True


def is_unique_no_additional_data_structures(input_str):
    """
    Variant of is_unique.  Uses no additional data structures (besides the variables from the iterator)
    Given:		Expect:
    tacos		True
    swag		True
    bobby		False
    california	False
    orbit       True
    e       True
    :param input_str: the string we want to check characters of
    :return: returns True if input_str has all unique characters, False otherwise
    """
    check_is_unique_input(input_str)
    for i, c in enumerate(input_str):
        if c in input_str[i+1:]:
            return False
    return True


class TestIsUniqueFunction(unittest.TestCase):
    def test_is_unique(self):
        self.assertFalse(is_unique("techqueria"))
        self.assertTrue(is_unique("tacos"))
        self.assertTrue(is_unique("swag"))
        self.assertFalse(is_unique("bobby"))
        self.assertFalse(is_unique("california"))
        self.assertTrue(is_unique("orbit"))
        self.assertTrue(is_unique("e"))
        with self.assertRaises(TypeError):
            is_unique(8)
        with self.assertRaises(ValueError):
            is_unique("")

    def test_is_unique_no_additional_data_structures(self):
        self.assertFalse(is_unique_no_additional_data_structures("techqueria"))
        self.assertTrue(is_unique_no_additional_data_structures("tacos"))
        self.assertTrue(is_unique_no_additional_data_structures("swag"))
        self.assertFalse(is_unique_no_additional_data_structures("bobby"))
        self.assertFalse(is_unique_no_additional_data_structures("california"))
        self.assertTrue(is_unique_no_additional_data_structures("orbit"))
        self.assertTrue(is_unique_no_additional_data_structures("e"))
        with self.assertRaises(TypeError):
            is_unique_no_additional_data_structures(8)
        with self.assertRaises(ValueError):
            is_unique_no_additional_data_structures("")


if __name__ == '__main__':
    unittest.main()
