# create a dictionary for a country of choice
# name, president, population, captital city

indonesia = {
    'name': 'Republik Indonesia',
    'president': 'IR. Joko Widodo',
    'population': 250000000,
    'capital_city': 'Jakarta'
}

print(indonesia['capital_city'])

indonesia['capital_city']='Kutai Kartanegara'

print(indonesia['capital_city'])

indonesia['continent'] = 'Asia'

print(indonesia)

for k in indonesia.keys():
    print("the {0} is {1}".format(k, indonesia[k] ))


# Indonesia:
# "the president is Joko Widodo"
# "the population is 250000000"

