"""
Python version 3.7.0
1.1
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
What if the input string is empty?
I assume that the user will input a non-empty string
If the string is empty, then raise a ValueError exception
If the input is NOT a string, then raise a TypeError exception

Given:		Expect:
tacos		true
swag		true
bobby		false
california	false
orbit		true
e		    true
"""
import unittest


def check_is_unique_input(input_str):
    if not isinstance(input_str, str):
        raise TypeError("expected string as input")
    if input_str == "":
        raise ValueError("empty input string")


def is_unique(input_str):
    check_is_unique_input(input_str)
    chars_seen = set()
    for c in input_str:
        if c in chars_seen:
            return False
        chars_seen.add(c)
    return True


def is_unique_no_additional_data_structures(input_str):
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
