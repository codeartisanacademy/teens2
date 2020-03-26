import datetime

# ask user to enter his/her birthday in the format of dd-mm-yyyy
bday_input = input("Enter your birthday in the format dd-mm-yyyy: ")

bday = datetime.datetime.strptime(bday_input, "%d-%m-%Y")

# tell her or him what day he / she was born, is it monday, or tuesday ...
print(bday.strftime("You were born on %A"))