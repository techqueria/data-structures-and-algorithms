# Implement an algorithm to determine if a string has all unique charactersself.
# What if you cannot use additional data structures.

# For this problem I will assume we are working ASCII characters for which there
# are 128 unique values.

import array

def isUnique(str):

    # if the string is longer than 128 characters, it means there are duplicates
    if len(str) > 128:
        return false

    # create an array to map the values
    mask = array.array('i',(0,)*128)

    for i in str:
        # the first time we find a character we change the value at that index
        # from 0 to 1
        if mask[ord(i)] == 0:
            mask[ord(i)] = 1
        # if the value at that index is already 1, it means this is a duplicate
        else:
            return False
    return True


print("%s" % (isUnique("test")))
print("%s" % (isUnique("abc123")))
