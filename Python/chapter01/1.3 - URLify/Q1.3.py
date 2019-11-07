import unittest


def replaceSpace(stringPas, totalLen):
    # Use replace() to search for blank sapces in the string
    # and replace with "%20"
    newString = stringPas.replace(' ',"%20")

    # Can use the length of string passed (second arg)
    # to check the length of new string is not greater
    # than original length
    if len(newString) > totalLen:
        return "Fail"
    else:
        return newString

class Test(unittest.TestCase):
    def test_perm_check(self):
        self.assertEqual(replaceSpace("Hi, how is your  ",18), "Fail")


if __name__ == '__main__':
    unittest.main()
