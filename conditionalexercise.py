# ask user to enter an email address
email = input("enter your email address: ")

# check if the email address is valid (has @ sign) - if valied says Email is valid
at_sign = email.count('@')

if at_sign > 0:
    print("your email is valid")
else:
    print("email is not valid")

# comparisson > >= < <= ==