# Implement an algorithm to determine if a string has all unique charactersself.
# What if you cannot use additional data structures.


def isUnique(string_):
    for i in range(len(string_)):
        i = 0
        for j in range(1,len(string_)):
            if string_[i] == string_[j]:
                return False
    return True

print(isUnique("GeeksforGeeks"))
#This soluation is O(n^2)

#let's see if we can go faster

def isUnique_(string_):
    d = {}
    for i in string_:
        if i in d:
            d[i] += 1

        else:
            d[i] = 1
    for keys,value in d.items():
        if value > 1:
            return False
    return True

print(isUnique_("camilo"))
