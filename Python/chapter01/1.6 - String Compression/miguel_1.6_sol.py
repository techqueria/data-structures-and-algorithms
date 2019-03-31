"""
Python version 3.7.0
1.6 - String Compression
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string, your method
should return the original string. You can assume the string has only uppercase and lowercase
letters (a-z).
"""
import unittest
from typing import Callable


def str_compression(s: str) -> str:
    """
    String compression will attempt to reduce the size of s by condensing
    s using the counts of repeated characters.
    Runtime: O(n), asymptotic runtime depends on size of s
    Space Complexity: O(n), compressed list
    :param s: the string we want to compress
    :return: the compressed string or s if the compressed string is not smaller
    """
    if len(s) == 0:
        return s
    compressed = []
    prev_char = s[0]
    count = 1
    for c in s[1:len(s)]:
        if c == prev_char:
            count += 1
            continue
        compressed.append(prev_char)
        compressed.append(str(count)[0])
        prev_char = c
        count = 1
    # clean up: last character count
    compressed.append(prev_char)
    compressed.append(str(count)[0])

    return ''.join(compressed) if len(compressed) < len(s) else s


class TestStringCompressionFunction(unittest.TestCase):
    def _run_tests(self, f: Callable[[str], str]) -> None:
        cases = [
            ('aabcccccaaa', 'a2b1c5a3'),
            ('abcde', 'abcde'),
            ('aabbccdd', 'aabbccdd'),
            ('', ''),
            ('c', 'c'),
            ('aaAAccCCCCC', 'a2A2c2C5')
        ]
        for s, expected in cases:
            self.assertEqual(f(s), expected, msg=(s, expected))

    def test_string_compression(self):
        self._run_tests(str_compression)


if __name__ == '__main__':
    unittest.main()
