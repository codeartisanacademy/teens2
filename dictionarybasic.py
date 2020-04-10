fc_bayern = {
    'goal_keeper': 'Michael Neuer',
    'left_defender': 'Philip Lahm',
    'striker': 'Lewandoski'
}

print(fc_bayern['goal_keeper'])

indonesia = {
    'name': 'Republik Indonesia',
    'president': 'Joko Widodo',
    'capital': 'Jakarta',
    'population': '250000000'
}

# access the value of a dictionary
print(indonesia['capital'])

indonesia['capital'] = 'Kutai Kartanegara'

print(indonesia['capital'])

indonesia['continent'] = 'Asia'

# iterate through the keys
for k in indonesia.keys() :
    print(k)

# iterate through the values
for v in indonesia.values():
    print(v)

