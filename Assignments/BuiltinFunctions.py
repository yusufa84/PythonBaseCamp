from functools import reduce

current = 'Complex'


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
if current == 'Reduce':
    print('Max: ' + str(reduce(max_find, lst)))


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