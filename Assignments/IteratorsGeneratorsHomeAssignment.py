# Problem 1
def gensquares(n):
    for num in range(n):
        yield num**2


for x in gensquares(10):
    print(x)

# Problem 2
import random
def rand_num(low,high,n):
    for num in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,5):
    print(num)

# Problem 3
s = 'hello'

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
