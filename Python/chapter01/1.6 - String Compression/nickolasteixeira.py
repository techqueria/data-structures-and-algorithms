#!/usr/bin/python3
import unittest


def string_compression(string):
    '''Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z). '''
    if not isinstance(string, str):
        return False

    new_str = ''
    count, new_count = 0, 0
    for idx in range(len(string) - 1):
        count += 1
        if string[idx] is not string[idx + 1]:
            new_str += string[idx]
            new_str += str(count)
            count = 0
        if idx is len(string) - 2:
            if string[idx] is string[idx + 1]:
                new_str += string[idx]
                new_str += str(count + 1)
            else:
                new_str += string[idx + 1]
                new_str += '1'

    for letter in new_str:
        if letter is '1':
            new_count += 1

    if len(string) // new_count is 1:
        return string
    return new_str


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(string_compression('aabcccccaaa'), 'a2b1c5a3')
        self.assertEqual(
            string_compression('bbaaaabcdeeefff'),
            'b2a4b1c1d1e3f3')
        self.assertEqual(string_compression('abcdef'), 'abcdef')
        self.assertNotEqual(string_compression('abcdef'), 'a1b1c1d1e1f1')


if __name__ == '__main__':
    unittest.main()
