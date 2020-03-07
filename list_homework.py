# create list literaly
countries = ['Singapore', 'Malaysia', 'Brunei']

# add one country
countries.append('Indonesia')

# insert at 2 position
countries.insert(1, 'Thailand')

# count 
print(len(countries))

countries.sort(reverse=True)

print(countries)

for country in countries:
    print(country.upper())

for x in range(1,10):
    print(x)