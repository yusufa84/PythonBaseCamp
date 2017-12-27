def palindrome(s):
    #Better way of doing the test
    return s == s[::-1]
    ''' Not so better way of doing the same thing
    count = 0
    flag = True
    while count < len(s):
       # print('Char: %s, s[len(s)-1]: %s' %(s[count],s[len(s)-count-1]))
        if s[count] != s[len(s)-count-1]:
            return False
        else:
            count += 1
    return flag
    '''
print(palindrome('helleh'))