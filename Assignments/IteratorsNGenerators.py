def gencube(n):
    for num in range(n):
        yield num ** 3

# for x in gencube(10):
    # print(x)

def genfibon(n):
    a = 1
    b = 1

    for i in range(n):
        # yield a
        # temp = a
        # a = b
        # b = temp + b
        # Doing the same thing using tuple unpacking
        yield a
        a, b = b, a + b

# for num in genfibon(10):
    # print(num)

def gen_simple():
    for x in range(3):
        yield x

g = gen_simple()
# print(next(g))
# print(next(g))
# print(next(g))


s = 'hello'

for letter in s:
    print(letter)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))