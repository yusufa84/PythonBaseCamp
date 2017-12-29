def func():
    return 1

#print(func())

s = 'This is a global variable'

def func():
    print(globals()['s'])

#func()

def hello(name='Yusuf'):
    print('Hello ' + name)

#hello()

greet = hello
#greet('Afini')
del hello
#greet('still there')

#Functions within functions
def new_hello(name='Yusuf'):
    print('The new_hello() function has been executed')

    def new_greet():
        return '\t This is inside the new_greet() function'

    def new_welcome():
        return '\t This is inside the new_welcome() function'

    print(new_greet())
    print(new_welcome())
    print('Now we are back inside the hello function')

#new_hello()

def again_hello(name='Yusuf'):
    def new_greet():
        return '\t This is inside the new_greet() function'

    def new_welcome():
        return '\t This is inside the new_welcome() function'

    if name == 'Yusuf':
        return new_greet
    else:
        return new_welcome

x = again_hello()
#print(x())

#Functions as arguments
def hello():
    return 'Hi Yusuf!'

def other(func):
    print('Other code goes here!')
    print(func())

#other(hello)

def new_decorator(func):
    def wrap_func(str):
        print('Code here, before executing the func')
        func(str)
        print('Code here will execute after the func')

    return wrap_func

def func_needs_decorator(str):
    print('This function needs a decorator->' + str)

func_needs_decorator('Do it')
func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator('Just do it')

#Another way of doing the above 3 steps
@new_decorator
def func_needs_decorator(str):
    print('This function needs a decorator-->' + str)
func_needs_decorator('Did it')