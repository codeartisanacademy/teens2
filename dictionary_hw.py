rounds = {
    'round1': 73,
    'round2': 80,
    'round3': 72,
    'round4': 70
}

total_score = 0
average_score = 0

#  "your total score is ...."
for score in rounds.keys():
    total_score = total_score + rounds[score]
# "your average score is ...."
average_score = total_score / len(rounds)

# total_score = sum(rounds.values)

print('total score: {0} '.format(total_score))
print('average score: {0}'.format(average_score))