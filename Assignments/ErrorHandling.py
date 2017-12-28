try:
    print(2 + '3')
except TypeError:
    print('There was a type error!')
finally:
    print('Finally this was printed')

try:
    f = open('testfile','r')
    f.write('Test write here')
except:
    print('Error in writing to the file')
else:
    print('File write was success')
finally:
    print('Always execute finally code block')


def askint():
    while True:
        try:
            val = int(input('Please enter an integer: '))
        except:
            print ('Looks like you did not enter an integer')
        else:
            print('Correct, that is an integer!')
            break
        finally:
            print('Finally executed')
    print(val)

askint()