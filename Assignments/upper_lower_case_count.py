def up_low(s):
    uppercase = 0
    lowercase = 0
    for c in s:
        if c.isupper():
            uppercase +=1
        elif c.islower():
            lowercase +=1
    print('Length of string = %s' %(len(s)))
    print('No. of Upper case characters = %s' %(uppercase))
    print('No. of Lower case characters = %s' %(lowercase))

up_low('Hello Mr.Rogers, how are you this fine Tuesday?')