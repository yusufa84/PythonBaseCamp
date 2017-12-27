def unique_list(l):
    unique = []
    for element in l:
        if element not in unique:
            unique.append(element)
    return unique

l = [1,1,1,1,2,2,3,3,3,4,5]
print(l)
print(unique_list(l))