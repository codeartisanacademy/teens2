import random

x = random.randint(0,10)
# ask user to enter a number
guess = input("enter your guess between 0-10: ")
# check if the number is equal with the random number, if yes say 'correct' if no say 'Wrong, the number was x
guess_int = int(guess)

if guess_int == x:
    print("Correct")
else:
    print("Wrong, the number was {0}".format(x))