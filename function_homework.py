x = input("Enter the first number: ")
y = input("Enter the second number: ")
operation = input("enter one of the commands (+ or - or * or /) : ")

def calculate(x, y, operation):
    x_int = int(x)
    y_int = int(y)
    
    if operation == '+':
        return x_int + y_int
    elif operation == '-':
        return x_int - y_int
    elif operation == '*':
        return x_int * y_int
    else:
        return x_int / y_int


result = calculate(x,y, operation)

print(result)