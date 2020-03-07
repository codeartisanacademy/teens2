# this is a string
"hello"

print(type("Hello"))

# variable - assigning a value to a variable
full_name = "john doe"

# string concatenation
print("Hello " + full_name)

# modify a variable
full_name = "jack bauer"
print("This is " + full_name)

# format function
greeting = "mr."

print("Hello {0} {1} how are you".format(greeting, full_name))
print("Hello {greet} {name} how are you".format(greet=greeting, name=full_name))

email = 'john@gmail.com'

print(email.count('@'))
print(email.index('@'))

