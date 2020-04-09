# create a function

# this is a function that do something without a parameter
def greet():
    print('hello')

# this is a function that do something with a parameter / argument
def greet_name(name):
    print('hello {0}'.format(name.title()))

# this is a function that returns something 
def addition(x, y):
    result = x + y
    return result

greet()

greet_name('jane')

z = addition(3,6)
print(z)
