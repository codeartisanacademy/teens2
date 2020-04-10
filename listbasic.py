# create a list literally

fruits = ["apple", "orange"]
fruits.append('durian')

print(len(fruits))

print(fruits)

print(fruits[1])

fruits.insert(1, "lychee")

print(fruits)

print(fruits[1])

# how to get the last item in the list
print(fruits[len(fruits)-1])
print(fruits[-1])
print(fruits)

print("there are {0} durian in my list".format(fruits.count('durian')))
print("Durian is at the position {0}".format(fruits.index('durian')))

for f in fruits:
    # Durian has 6 characters
    print('---------------------------')
    print("{0} has {1} characters".format(f, len(f)))

print('xxxxxxxxxx')

fruits.remove('orange')

print(fruits)