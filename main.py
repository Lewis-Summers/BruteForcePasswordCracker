def check(guess1):
    if guess1 == pas:
        return 'yes'
    else:
        return 'no'

def lts(string):
    str1 = ''
    for t in string:
        str1 += t
    return str1

def reper():
    for letter in alpha:
        if rep:
            guess.append(hi)
            guess.append(letter)
            print(lts(guess))


pas = input('Whats your password: ')

dd = input('Welcome to the password cracker!\n1 for only letters,\n2 for only numbers,\n3 for all characters,\n')

if dd == '1':
    alpha = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G',
             'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
elif dd == '2':
    alpha = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
elif dd == '3':
    alpha = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '`', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i',
             'o', 'p', '[', ']', '\\', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b',
             'n', 'm', ',', '.', '/', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Q', 'W', 'E',
             'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"',
             'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']
elif dd == '0':
    alpha = ''
    print('bye')
    quit()
else:
    alpha = ''
    print('Print sorry theres been a issue')
    quit()

guess = []


inside = True

layer = 0
layer2 = 0
rep = True
while inside:
    if len(alpha) - 1 == layer:
        layer2 += 1
        print(layer2, 'Increasing')
        layer = 0
    else:
        layer += 1
    hi = alpha[layer]
    print(layer, hi)

    if layer2 == 1:
        for letter in alpha:
            if rep:
                guess.append(hi)
                guess.append(letter)
                print(lts(guess))
                if check(lts(guess)) == 'yes':
                    inside = False
                    rep = False
                    print(lts(guess))
                    print('endloop1')
                else:
                    guess.clear()
    if layer2 == 2:
        for letter in alpha:
            if rep:
                for let in alpha:
                    if rep:
                        guess.append(hi)
                        guess.append(letter)
                        guess.append(let)
                        print(lts(guess))
                        if check(lts(guess)) == 'yes':
                            inside = False
                            rep = False
                            print(lts(guess))
                            print('endloop1')
                        else:
                            guess.clear()
    if layer2 == 3:
        for letter in alpha:
            if rep:
                for let in alpha:
                    if rep:
                        for leta in alpha:
                            if rep:
                                guess.append(hi)
                                guess.append(letter)
                                guess.append(let)
                                guess.append(leta)
                                print(lts(guess))
                                if check(lts(guess)) == 'yes':
                                    inside = False
                                    rep = False
                                    print(lts(guess))
                                    print('endloop1')
                                else:
                                    guess.clear()

    if layer2 == 4:
        for letter in alpha:
            if rep:
                for let in alpha:
                    if rep:
                        for leta in alpha:
                            if rep:
                                for lety in alpha:
                                    if rep:
                                        guess.append(hi)
                                        guess.append(letter)
                                        guess.append(let)
                                        guess.append(leta)
                                        guess.append(lety)
                                        print(lts(guess))
                                        if check(lts(guess)) == 'yes':
                                            inside = False
                                            rep = False
                                            print(lts(guess))
                                            print('endloop1')
                                        else:
                                            guess.clear()
    if layer2 == 5:
        for letter in alpha:
            if rep:
                for let in alpha:
                    if rep:
                        for leta in alpha:
                            if rep:
                                for lety in alpha:
                                    if rep:
                                        for lett in alpha:
                                            if rep:
                                                guess.append(hi)
                                                guess.append(letter)
                                                guess.append(let)
                                                guess.append(leta)
                                                guess.append(lety)
                                                guess.append(lett)
                                                print(lts(guess))
                                                if check(lts(guess)) == 'yes':
                                                    inside = False
                                                    rep = False
                                                    print(lts(guess))
                                                    print('endloop1')
                                                else:
                                                    guess.clear()
    if layer2 == 6:
        for letter in alpha:
            if rep:
                for let in alpha:
                    if rep:
                        for leta in alpha:
                            if rep:
                                for lety in alpha:
                                    if rep:
                                        for lett in alpha:
                                            if rep:
                                                for let8 in alpha:
                                                    if rep:
                                                        guess.append(hi)
                                                        guess.append(letter)
                                                        guess.append(let)
                                                        guess.append(leta)
                                                        guess.append(lety)
                                                        guess.append(lett)
                                                        guess.append(let8)
                                                        print(lts(guess))
                                                        if check(lts(guess)) == 'yes':
                                                            inside = False
                                                            rep = False
                                                            print(lts(guess))
                                                            print('endloop1')
                                                        else:
                                                            guess.clear()


    if layer2 == 7:
        for letter in alpha:
            if rep:
                for let in alpha:
                    if rep:
                        for leta in alpha:
                            if rep:
                                for lety in alpha:
                                    if rep:
                                        for lett in alpha:
                                            if rep:
                                                for let8 in alpha:
                                                    if rep:
                                                        for letg in alpha:
                                                            if rep:
                                                                guess.append(hi)
                                                                guess.append(letter)
                                                                guess.append(let)
                                                                guess.append(leta)
                                                                guess.append(lety)
                                                                guess.append(lett)
                                                                guess.append(let8)
                                                                guess.append(letg)
                                                                print(lts(guess))
                                                                if check(lts(guess)) == 'yes':
                                                                    inside = False
                                                                    rep = False
                                                                    print(lts(guess))
                                                                    print('endloop1')
                                                                else:
                                                                    guess.clear()
    if layer2 == 8:
        for letter in alpha:
            if rep:
                for let in alpha:
                    if rep:
                        for leta in alpha:
                            if rep:
                                for lety in alpha:
                                    if rep:
                                        for lett in alpha:
                                            if rep:
                                                for let8 in alpha:
                                                    if rep:
                                                        for letg in alpha:
                                                            if rep:
                                                                for letl in alpha:
                                                                    if rep:
                                                                        guess.append(hi)
                                                                        guess.append(letter)
                                                                        guess.append(let)
                                                                        guess.append(leta)
                                                                        guess.append(lety)
                                                                        guess.append(lett)
                                                                        guess.append(let8)
                                                                        guess.append(letg)
                                                                        guess.append(letl)
                                                                        print(lts(guess))
                                                                        if check(lts(guess)) == 'yes':
                                                                            inside = False
                                                                            rep = False
                                                                            print(lts(guess))
                                                                            print('endloop1')
                                                                        else:
                                                                            guess.clear()
    if layer2 == 9:
        for letter in alpha:
            if rep:
                for let in alpha:
                    if rep:
                        for leta in alpha:
                            if rep:
                                for lety in alpha:
                                    if rep:
                                        for lett in alpha:
                                            if rep:
                                                for let8 in alpha:
                                                    if rep:
                                                        for letg in alpha:
                                                            if rep:
                                                                for letl in alpha:
                                                                    if rep:
                                                                        for letA in alpha:
                                                                            if rep:
                                                                                guess.append(hi)
                                                                                guess.append(letter)
                                                                                guess.append(let)
                                                                                guess.append(leta)
                                                                                guess.append(lety)
                                                                                guess.append(lett)
                                                                                guess.append(let8)
                                                                                guess.append(letg)
                                                                                guess.append(letl)
                                                                                guess.append(letA)
                                                                                print(lts(guess))
                                                                                if check(lts(guess)) == 'yes':
                                                                                    inside = False
                                                                                    rep = False
                                                                                    print(lts(guess))
                                                                                    print('endloop1')
                                                                                else:
                                                                                    guess.clear()
    if layer2 == 10:
        for letter in alpha:
            if rep:
                for let in alpha:
                    if rep:
                        for leta in alpha:
                            if rep:
                                for lety in alpha:
                                    if rep:
                                        for lett in alpha:
                                            if rep:
                                                for let8 in alpha:
                                                    if rep:
                                                        for letg in alpha:
                                                            if rep:
                                                                for letl in alpha:
                                                                    if rep:
                                                                        for letA in alpha:
                                                                            if rep:
                                                                                for leth in alpha:
                                                                                    if rep:
                                                                                        guess.append(hi)
                                                                                        guess.append(letter)
                                                                                        guess.append(let)
                                                                                        guess.append(leta)
                                                                                        guess.append(lety)
                                                                                        guess.append(lett)
                                                                                        guess.append(let8)
                                                                                        guess.append(letg)
                                                                                        guess.append(letl)
                                                                                        guess.append(letA)
                                                                                        guess.append(leth)
                                                                                        print(lts(guess))
                                                                                        if check(lts(guess)) == 'yes':
                                                                                            inside = False
                                                                                            rep = False
                                                                                            print(lts(guess))
                                                                                            print('endloop1')
                                                                                        else:
                                                                                            guess.clear()
                                                                        
    if check(hi) == 'yes':
        inside = False
        print('endloop')

print('end')
print(lts(guess))
