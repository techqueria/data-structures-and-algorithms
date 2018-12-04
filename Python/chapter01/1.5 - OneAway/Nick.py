#!/usr/bin/python3
import unittest


def one_away(s1, s2):
    '''Given two strings, write a function to check if
    they are one edit (or zero edits) away.'''
    if abs(len(s1) - len(s2)) > 1:
        return False

    str1 = s1 if len(s1) < len(s2) else s2
    str2 = s2 if len(s1) < len(s2) else s1
    idx1, idx2 = 0, 0
    diff = False

    while idx1 < len(str1) and idx2 < len(str2):
        if str1[idx1] is not str2[idx2]:
            if diff:
                return False
            diff = True

            if len(str1) is len(str2):
                idx1 += 1
        else:
            idx1 += 1
        idx2 += 1

    return True


class Test(unittest.TestCase):
    def test1(self):
        s1 = "Tact Cat"
        s2 = "TactCat"
        s3 = "nick"
        s4 = "jeff"
        self.assertTrue(one_away(s1, s2))
        self.assertFalse(one_away(s3, s4))


if __name__ == '__main__':
    unittest.main()
