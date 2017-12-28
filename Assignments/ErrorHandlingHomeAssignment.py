try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print('Cannot square non numeric values')

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print('Cannot divide by zero')
finally:
    print('All done')

def ask():
    while True:
        try:
            val = int(input('Enter an integer'))
        except:
            print("That's not an integer")
            continue
        else:
            print("Thank you, you number squared is: %s" %(val**2))
            break

ask()