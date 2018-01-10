import re

patterns = ['term1','term2']

text = 'This is a string with term1, but not the other term'

print(re.search('hello','hello world'))

for pattern in patterns:
    print('Searching for "%s" in : \n"%s"' %(pattern, text))

    if re.search(pattern,text):
        print('\nMatch was found.\n')
    else:
        print('\nNo match was found.\n')

match = re.search(patterns[0],text)
print(match.start())
print(match.end())

split_term = '@'
phrase = 'What is your email, is it hello@gmail.com?'
print(re.split(split_term,phrase))

print(len(re.findall('match','Here is one match, here is another match')))

def multi_re_find(patterns,phrase):
    '''
    Multi re find method
    :param patterns: list
    :param phrase: string
    :return: Nothing
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %pattern)
        print(re.findall(pattern,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dssss...sdddd'
test_patterns = ['sd*',         # s followed by zero or more d's
                 'sd+',         # s followed by one or more d's
                 'sd?',         # s followed by zero or one d's
                 'sd{3}',       # s followed by three d's
                 'sd{2,3}']     # s followed by two to three d's

multi_re_find(test_patterns,test_phrase)


test_phrase = 'This is a string! But it has punctutation. How can we remove it'
print(re.findall('[^!.? ]+', test_phrase))

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns = ['[a-z]+',  # sequences of lower case letters
                 '[A-Z]+',  # sequences of upper case letters
                 '[a-zA-Z]+',  # sequences of lower or upper case letters
                 '[A-Z][a-z]+']  # one upper case letter followed by lower case letters

multi_re_find(test_patterns, test_phrase)