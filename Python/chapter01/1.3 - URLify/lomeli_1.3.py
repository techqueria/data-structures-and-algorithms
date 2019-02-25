# Write a method to replace all spaces in a string with '%20'
# "Mr John Smith     ", 13 => "Mr%20John%20Smith"

def Urlify(string, size):
    temp = []
    url = '%20'
    for i in range(size):
        if string[i] == ' ':
            temp.append(url)
        else:
            temp.append(string[i])
    return ''.join(temp)

print(Urlify("Mr John Smith     ", 13))
