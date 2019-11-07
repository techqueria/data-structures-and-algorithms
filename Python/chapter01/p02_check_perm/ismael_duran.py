import unittest


def check_perm(example, example2):
    for letter in example:
        if letter in example2:
            index = example2.index(letter)
            example2 = example2[:index] + example2[index+1:]

            if example2 == '':
                return True
            else:
                continue
        else:
            return False


class Test(unittest.TestCase):
    def test_perm_check(self):
        self.assertFalse(check_perm("hello", "ehloe"))


if __name__ == '__main__':
    unittest.main()
