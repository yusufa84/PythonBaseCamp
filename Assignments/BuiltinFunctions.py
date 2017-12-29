from functools import reduce

current = 'Assignment'


# Map()
def fahrenheit(T):
    return (9.0 / 5) * T + 32


if current == 'Map':
    print(fahrenheit(0))

temp = [0, 22.5, 40, 100]
if current == 'Map':
    print(list(map(lambda T: (9.0 / 5) * T + 32, temp)))

a = [1, 2, 3]
if current == 'Map':
    print(list(map(lambda num: num * -1, a)))

# Reduce
lst = [34, 21, 23, 24, 101, 2332, 1, 22]
if current == 'Reduce':
    print(max(lst))
    max_find = lambda a, b: a if (a > b) else b
    print('Max: ' + str(reduce(max_find, lst)))
    mylist = [47,11,42,13]
    print(reduce(lambda x,y: x+y,mylist))


# filter
def even_check(num):
    return num % 2 == 0

if current == 'Filter':
    print(even_check(32))
    print(list(filter(even_check, lst)))

# Zip
x = [1, 2, 3]
y = [4, 5, 6]
if current == 'Zip':
    print(list(zip(x, y)))

a = [1, 2, 3, 4, 5]
b = [2, 2, 10, 1, 1]
if current == 'Zip':
    for pair in zip(a, b):
        print(max(pair))

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
if current == 'Zip':
    print(list(zip(d2, d1.values())))

# Enumerate
l = ['a', 'b', 'c']
if current == 'Enum':
    for (count, item) in enumerate(l):
        print(count)
        print(item)

if current == 'Enum':
    for count, item in enumerate(l):
        if count >= 2:
            break
        else:
            print(item)

# all() and any()
l = [True, True, False, False]
if current == 'AllNAny':
    print(all(l))
    print(any(l))

#Complex
if current == 'Complex':
    print(complex(2,3))
    print(complex('10+2j'))

if current == 'Assignment':
    #Problem 1
    def word_lengths(phrase):
        return list(map(lambda word: len(word), phrase.split(' ')))

    print(word_lengths('How long are the words in this phrase'))

    #Problem 2
    def digits_to_num(digits):
        return reduce(lambda x, y: x*10 + y, digits)

    print(digits_to_num([3,4,3,2,1]))

    #Problem 3
    def filter_words(word_list, target_letter):
        return list(filter(lambda word: str(word[0]).lower()==target_letter.lower(),word_list))

    l = ['hello', 'are', 'cat', 'Goat', 'ham', 'hi', 'go', 'to', 'heart']
    print(filter_words(l,'g'))

    #Problem 4
    def concatenate(L1, L2, connecter):
        return [word1+connecter+word2 for (word1,word2) in zip(L1,L2)]
        pass
    print(concatenate(['A','B'],['a','b'],'-'))

    #Problem 5
    def d_list(L):
        return {key:value for value,key in enumerate(L)}
    print(d_list(['a','b','c']))

    #Problem 6
    def count_match_index(L):
        return len([num for count,num in enumerate(L) if num == count])

    print(count_match_index([0,2,2,1,5,5,6,10]))