import datetime

def parse_disc(line):
    import re

    matches = re.match('Disc \#\d+ has (\d+) positions; at time=0, it is at position (\d+).', line)

    return int(matches.group(1)), int(matches.group(2))


def discs_allow_through_at(time):
    global discs

    for idx, disc in enumerate(discs):
        if (disc[1] + time + idx + 1) % disc[0] != 0:
            return False

    return True


start_time = datetime.datetime.now()

discs = []
for line in open('input','r'):
    discs.append(parse_disc(line.strip()))

time = 0

while True:
    if discs_allow_through_at(time):
        break

    time += 1

print time

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
