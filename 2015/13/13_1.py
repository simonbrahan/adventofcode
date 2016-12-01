import re
import itertools

def get_cmd(line):
    pattern = re.compile('(\w+?) would (lose|gain) (\d+?) happiness units by sitting next to (\w+).')
    res = re.search(pattern, line)

    if res.group(2) == 'gain':
        happiness = int(res.group(3))
    else:
        happiness = 0 - int(res.group(3))

    return {
        'person': res.group(1),
        'happiness': happiness,
        'neighbour': res.group(4),
    }

ex_input = open('input.txt', 'r')

happiness_deltas = {}
for line in ex_input:
    cmd = get_cmd(line)
    if cmd['person'] not in happiness_deltas:
        happiness_deltas[cmd['person']] = {}

    if cmd['neighbour'] not in happiness_deltas[cmd['person']]:
        happiness_deltas[cmd['person']][cmd['neighbour']] = 0

    happiness_deltas[cmd['person']][cmd['neighbour']] += cmd['happiness']

    if cmd['neighbour'] not in happiness_deltas:
        happiness_deltas[cmd['neighbour']] = {}

    if cmd['person'] not in happiness_deltas[cmd['neighbour']]:
        happiness_deltas[cmd['neighbour']][cmd['person']] = 0

    happiness_deltas[cmd['neighbour']][cmd['person']] += cmd['happiness']

happiest_score = 0
for combo in itertools.permutations(happiness_deltas.keys()):
    seating_happiness = 0
    seating = list(combo)
    seating.append(seating[0])
    prev_person = None

    for person in seating:
        if prev_person:
            seating_happiness += happiness_deltas[prev_person][person]
        prev_person = person

    if seating_happiness > happiest_score:
        happiest_score = seating_happiness

print happiest_score
