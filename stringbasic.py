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

# Hello mr. jack bauer how are you
# format with index place holder
print("Hello {0} {1} how are you".format(greeting, full_name))
# format with labeled place holder
print("Hello {greet} {name} how are you".format(greet=greeting, name=full_name))


text = "Hi Everyone how is everyone doing today"
print(text.lower().count('everyone'))

email = 'john@gmail.com'
print(email.index('@'))

print(email.replace('john', 'mike'))
print(email.startswith('budi'))
print(email.isalpha())
print("1212abc".isalnum())
print("121313".isnumeric())
print("this a text".find("a"))
print("   hello    ".strip())

