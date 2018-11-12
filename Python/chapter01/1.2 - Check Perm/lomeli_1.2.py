# Given two strings, write a method to decide if one is a permutation of the other

def isPermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    sort1 = sorted(str1)
    sort2 = sorted(str2)

    return sort1 == sort2

print("%s" % (isPermutation("stop", "pots")))
print("%s" % (isPermutation("stops", "ponds")))
