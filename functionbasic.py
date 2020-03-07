# create a function

def greet():
    print('hello')

def greet_name(name):
    print('hello {0}'.format(name.title()))

def addition(x, y):
    result = x + y
    return result

greet()

greet_name('jane')

z = addition(3,6)
print(z)
