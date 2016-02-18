input_sequence = '3113322113'

from itertools import groupby

def look_and_say(s):
    new_s = []
    for c, l in groupby(s):
        new_s.append(str(len(list(l))))
        new_s.append(c)
    return ''.join(new_s)

for i in range(40):
    input_sequence = look_and_say(input_sequence)

print len(input_sequence)
