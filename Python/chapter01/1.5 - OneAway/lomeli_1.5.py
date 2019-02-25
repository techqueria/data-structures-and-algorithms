# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character
# Given two strings, write a function to check if they are one edit
# (or sero edits) away.

# Example
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

def OneAway(str1, str2):
    if len(str1) >= len(str2):
        bigStr = str1
        smallStr = str2
    else:
        bigStr = str2
        smallStr = str1

    for c in smallStr:
        bigStr = bigStr.replace(c,'')

    return len(bigStr) <= 1

print(OneAway("pale", "ple"))
print(OneAway("pales", "pale"))
print(OneAway("pale", "bale"))
print(OneAway("pale", "bake"))
