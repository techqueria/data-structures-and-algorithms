"""
1.6:String Compression: Implement a method to perform basic string compression using
 the counts of repeated characters. For example, the string aabcccccaaa would
 become a2blc5a3. If the "compressed" string would not become smaller than the
 original string, your method should return
the original string. You can assume the string has only uppercase and lowercase
letters (a - z).
"""



def string_compression(str1):
    count = 1
    new_str = ""
    for i in range(len(str1)-1):
        if(str1[i] == str1[i+1]):
            count+=1
        else:
            new_str += str1[i] + str(count)
            count = 1
    new_str += str1[i] + str(count)

    if len(new_str) < len(str1):
        return new_str

    else:
        return str1








print(string_compression('aabcccccaaa'))
