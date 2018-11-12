example = "hello"
example2 = "ehloe"

for letter in example:
    if letter in example2:
            index = example2.index(letter)
            example2 = example2[:index] + example2[index+1:]
            print(example2)

            if example2 == '':
                print("done with permutation")
                break
            else:
                continue
    else:
        print("Not permutatable")
        break
        
