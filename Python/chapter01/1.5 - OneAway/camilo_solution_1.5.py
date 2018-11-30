"""
One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character. Given two
strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
Hints:#23, #97, #130
"""

def oneAway(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    d = {}
    for i in str1:
        if i in d:
            d[i] =+ 1
        else:
            d[i] = 1

    for j in str2:
        if j in d:
            d[j] -= 1

        else:
            d[j] = 1
    count = 0# count the number of times


    """
    My thought on how to do this:
    So knowing the pale and ple
    when we subtract it from the hash table we know there should be a value of 1
    for removal of one letter

    The insertation of one letter should only leave the key of one
    pales and pale

    The interseting stuff happens when you have a change of letter.
    The letter gets counting when you place it in the hash table
    pale bale.
    We use count to count the number of time count can be one. You'll find
    that replaceing a letter is going to make count two v's of one

    replacing two letter will make v's count more onces

    You'll see this when you print k and v
    
    """
    for k,v in d.items():
        #print(k,v)
        if v == 1:
            count += 1

    if count <= 2 : #
        return True

    else:
        return False









print(oneAway('pale', 'ple'))#True
print(oneAway('pales', 'pale'))#True
print(oneAway('pale', 'bale'))#True

print(oneAway('pale', 'bake'))#False
