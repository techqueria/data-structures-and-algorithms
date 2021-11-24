# Implement a method to perform basic string compression using the counts
# of repeated characters.  If the "compressed" string would not become smaller
# than the original string, your method should return the original stringself.
# You can assume that the string has only uppercase and lowercase letters.

def stringCompress(st):
    result = []
    cur = st[0]
    count = 0
    for i in range(len(st)):
        if cur == st[i]:
            count = count + 1
        else:
            result.append(cur)
            result.append(str(count))
            cur = st[i]
            count = 1
    result.append(cur)
    result.append(str(count))
    comp = ''.join(result)
    if len(comp) < len(st):
        return comp
    else:
        return st

print(stringCompress("aabcccccaaa"))
print(stringCompress("aabca"))
print(stringCompress("XxxyyyZZzzzzz"))
print(stringCompress("abc"))
