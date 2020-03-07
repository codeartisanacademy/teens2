# ask user to enter a number, store it inside variable x
x = input('Enter the first number: ')
# ask user to enter another number, store it inside variable y
y = input('Enter the second number: ')
# ask user to enter the result of multiplication of x and y
result = input('Enter the result for multiplication of {0} * {1}: '.format(x, y))
# print out "The result is correct" or "The result is wrong"
x_int = int(x) 
y_int = int(y)
# notes: this is math operation in python *, +, -, /
# notes: comparison ==, >, <, >=, <=, !=
if int(result) == x_int * y_int:
    print("Correct")
else:
    print("Wrong")