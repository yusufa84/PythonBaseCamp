import string

def ispangram(str1):
    print(str1)
    alphabet = string.ascii_lowercase
    for char in alphabet:
        if str1.count(char) <= 0:
            print('The entered string is not pangram')
            break
    else:
        print('The entered string is a pangram')

    '''
    *** Another way of doing the same thing as per the trainer ***
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
    '''

ispangram('The quick brown fox jumps over the lazy dog')