# ask user to enter the first number
x = input('enter the first number: ')
# ask user to enter the second number
y = input('enter the second number: ')
# calculate the multiplication of that number. You need to create a function to calculate
def multiply(x,y):
    x_int = int(x)
    y_int = int(y)
    return x_int * y_int

result = multiply(x,y)

print(result)
