# Counter
from collections import Counter

l = [1,1,1,1,2,2,2,3,4,5,4,5]

print(Counter(l))

s = 'assasdxXXCACAxzczxcasdaADASDASDAsdazx'
print(Counter(s))

s = 'How many times does each word show up in this sentence word word shoe up up'
words = s.split()
c = Counter(words)
print(c)
print(c.most_common(3))
print(sum(c.values()))

# defaultdict
from collections import defaultdict
d = {'k1': 1}
print(d['k1'])

d = defaultdict(object)
print(d['k3'])

# Use with lambda
d = defaultdict(lambda: 0)
print(d['k2'])

# ordered dict
dict = {}
dict['a'] = 1
dict['b'] = 2
dict['c'] = 3
dict['d'] = 4
dict['e'] = 5

for k, v in dict.items():
    print(k, v)

from collections import OrderedDict
dict = OrderedDict()
dict['a'] = 1
dict['b'] = 2
dict['c'] = 3
dict['d'] = 4
dict['e'] = 5

for k, v in dict.items():
    print(k, v)

# Without being ordereddict both d1 and d2 are same irrespective of the order of key value pairs
d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print('Are both same? ')
print( d1 == d2)

# With being ordereddict both d1 and d2 are no longer same as the order of key value pairs is different
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print('Are both ordereddict same? ')
print( d1 == d2)

# namedtuple
t = (1, 2, 3)
print(t[0])

from collections import namedtuple
Dog = namedtuple('Dog','age breed name')
sam = Dog(age=2,breed='Lab',name='Sammy')
print(sam)
print(sam.age)
print(sam.breed)
print(sam.name)
print(sam[0])

Cat = namedtuple('Cat','fur claws name')
c = Cat(fur='Fuzzy', claws=False, name='Kitty')
print(c)
