"""
String Rotation:Assume you have a method isSubstring which checks if one word is a
substring of another. Given two strings, sl and s2, write code to check if s2 is
a rotation of sl using only one call to isSubstring (e.g.,"waterbottle" is a
rotation of"erbottlewat").
"""

def isSubstring(s1,s2):
    if s2 in s1: #check to see if the seqence of s2 is found in s1
        return True
    return False

def Rotation(s1,s2):
    """
    if they are substring of each other then we first check its lenght
    """
    if len(s1) != len(s2): #if there not the same lenght then there different woulds
        return False

    else:
        s1+=s1 #waterbottlewaterbottle Anyroataion can be found here
        return isSubstring(s1,s2)

s1 = "waterbottle"
s2 = "erbottlewat"

print(Rotation(s1,s2))
