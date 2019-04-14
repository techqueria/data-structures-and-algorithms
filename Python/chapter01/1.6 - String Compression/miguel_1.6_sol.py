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
    for c in s[1:]:
        if c == prev_char:
            count += 1
            continue
        compressed.append(f'{prev_char}{count}')
        prev_char = c
        count = 1
    # clean up: last character count
    compressed.append(f'{prev_char}{count}')
    compressed = ''.join(compressed)
    if len(compressed) >= len(s):
        return s
    return compressed


class TestStringCompressionFunction(unittest.TestCase):
    def test_string_compression(self):
        cases = [
            ('aabcccccaaa', 'a2b1c5a3'),
            ('abcde', 'abcde'),
            ('aabbccdd', 'aabbccdd'),
            ('', ''),
            ('c', 'c'),
            ('aaAAccCCCCC', 'a2A2c2C5'),
            ('aaaaaaaaaa', 'a10')
        ]
        for s, expected in cases:
            self.assertEqual(str_compression(s), expected, msg=(s, expected))


if __name__ == '__main__':
    unittest.main()
