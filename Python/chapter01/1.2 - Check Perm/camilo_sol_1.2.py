"""
Check Permutation: Given two strings,write a method to decide if
one is a permutation of the other.
"""




def perm_check(str_1,str_2):
    if len(str_1) != len(str_2):#If both str are diiferent lenghts return false
        return False
    d = {}
    for i in str_1: #takes all the letter in string one and add them to the hash map
        if i in d:  #counts the number of letter
            d[i] += 1
        else:
            d[i] = 1

    for j in str_2: #
        if j in d:#Looks at the letter in the string and subtract the number
                  #of the same letter from the value
            d[j] -= 1
        else:
            d[j] = 1

    for keys,value in d.items():
        if value > 0:
            return False
    return True


#O(n) sol?
print(perm_check("camilo","pop")) #False

print(perm_check("camilo","camplo")) #false

print(perm_check("camilo","olimac")) #True
