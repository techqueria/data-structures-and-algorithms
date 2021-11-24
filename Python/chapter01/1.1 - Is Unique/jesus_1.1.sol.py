import unittest


def is_unique(s: str) -> bool:
    for x in s:
        if s.count(x) > 1:
            return False
    return True

class TestIsUnique(unittest.TestCase):

    def test_is_unique(self):
        self.assertEqual(is_unique('aaaaa'), False)
        self.assertEqual(is_unique('abc'), True)
        self.assertEqual(is_unique('abcda'), False)
        self.assertEqual(is_unique('jhfbwej'), False)
        self.assertEqual(is_unique(''), True)
        self.assertEqual(is_unique('a'), True)


if __name__ == '__main__':
    unittest.main()