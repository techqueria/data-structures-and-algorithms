import unittest

# Note that this solution assumes a unique string
# implies a lowercase letter and the uppercase of
# that letter is not considered duplicates
# example: the string "Hather" has an uppercase "H"
#          and lowercase "h" yet the string has no duplicate
#          "h" or "H"


def uniqueChar(passedStr):

        # Will use the built-in function set() which
        # eliminates dupplicates
        deleteDuplicateIfAny = set(passedStr)

        # If the string had unique characters the string
        # length remains the same
        # If the string has duplicates then size
        if len(deleteDuplicateIfAny) == len(passedStr):
                return "Unique"
        else:
                return "Not Unique"


class Test(unittest.TestCase):
    def test_uniqueChar(self):
        example = "Helloh"
        self.assertEqual(uniqueChar(example), "Not Unique")


if __name__ == '__main__':
    unittest.main()
