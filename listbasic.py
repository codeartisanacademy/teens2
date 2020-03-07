# create a list literally
fruits = ["apple", "orange"]

fruits.append('durian')

print(len(fruits))
fruits.insert(1, 'rambutan')
# get the first item from the list
print(fruits[0])

# how to get the last item in the list
print(fruits[len(fruits)-1])
print(fruits[-1])
print(fruits)

print("there are {0} durian in my list".format(fruits.count('durian')))
print("Durian is at the position {0}".format(fruits.index('durian')))

for f in fruits:
    # Durian has 6 characters
    print("{0} has {1} characters".format(f, len(f)))
