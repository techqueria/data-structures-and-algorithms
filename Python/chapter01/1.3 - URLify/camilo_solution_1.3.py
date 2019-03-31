"""
URLify: Write a method to replace all spaces in a string with '%20'. You may
 assume that the string has sufficient space at the end to hold the additional
 characters,and that you are given the "true" length of the string.
 (Note: If implementing in Java,please use a character array so that you can
 perform this operation in place.)
EXAMPLE
Input: "Mr John Smith   ", 13 Output: "Mr%20John%20Smith"
"""

def urlify(str):
    len_ = len(str) #gets the lenght of str
    new_str = ""#build a new string
    for i in range(len_-1):
        if str[i] == " " and str[i+1]==" ":#if two space aheah are space then break
            break
        if str[i] == " ": #if we find a space just add %20
            new_str+= "%20"

        else: #just add the chars
            new_str+= str[i]

    return new_str

print(urlify("MY house is on fire "))
