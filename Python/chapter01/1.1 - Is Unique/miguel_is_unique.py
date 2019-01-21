"""
Python version 3.7.0
1.1
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

Given:		Expect:
tacos		true
swag		true
bobby		false
california	false
orbit		true
e		    true
"""


def is_unique(input_str):
    freqs = {}
    for c in input_str:
        if c not in freqs:
            freqs[c] = 1
        else:
            return False
    return True


def is_unique_no_additional_data_structures(input_str):
    for i in range(0, len(input_str)):
        for j in range(i+1, len(input_str)):
            if input_str[i] == input_str[j]:
                return False
    return True


def main():
    test1 = "tacos"
    test2 = "swag"
    test3 = "bobby"
    test4 = "california"
    test5 = "orbit"
    test6 = "e"

    # run tests, want to get all 'True' in the console output
    print(is_unique(test1) == True)
    print(is_unique(test2) == True)
    print(is_unique(test3) == False)
    print(is_unique(test4) == False)
    print(is_unique(test5) == True)
    print(is_unique(test6) == True)

    print(is_unique_no_additional_data_structures(test1) == True)
    print(is_unique_no_additional_data_structures(test2) == True)
    print(is_unique_no_additional_data_structures(test3) == False)
    print(is_unique_no_additional_data_structures(test4) == False)
    print(is_unique_no_additional_data_structures(test5) == True)
    print(is_unique_no_additional_data_structures(test6) == True)


if __name__ == '__main__':
    main()
