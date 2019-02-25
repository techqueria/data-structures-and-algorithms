# Given a string, write a function to check if it is a permutation of a palindrome
# A palindrome is a word or phrase that is the same forwards and backwards
# A permutation is a rearrangement of lettersself.
# The palindrome does not need to be limited to dictionary words

#Example Tact toa => True

def PalinPerm(str):
    # Make all letters lowercase
    str = str.lower()
    # Remove spaces from string
    str = ''.join(str.split())
    uniq = set(c for c in str)

    if len(str) % 2 != 0:
        return (len(str) / 2)+1 == len(uniq)
    else:
        return (len(str) / 2) == len(uniq)

print(PalinPerm("Tact toa"))
print(PalinPerm("reca Cra"))
print(PalinPerm("Taco dog"))
print(PalinPerm("ab Ba"))
print(PalinPerm("abcdba"))
