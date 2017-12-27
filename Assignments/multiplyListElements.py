def multiply(numbers):
    product = 1
    for num in numbers:
        product = product * num
    return product

l = [1,2,3,-4]
print(multiply(l))