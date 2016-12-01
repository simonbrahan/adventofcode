import re

class Player:
    name = ''
    speed = 0
    uptime = 0
    downtime = 0

    def __init__(self, name, speed, uptime, downtime):
        self.name = name
        self.speed = speed
        self.uptime = uptime
        self.downtime = downtime

    def get_cycle_time(self):
        return self.uptime + self.downtime


def get_cmd(line):
    pattern = re.compile('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    res = re.search(pattern, line)

    player = Player(
        res.group(1),
        int(res.group(2)),
        int(res.group(3)),
        int(res.group(4)),
    )

    return player

def give_points(distances, points):
    distances.sort(key = lambda val: val['distance'])
    distances.reverse()
    max_distance = 0
    for distance in distances:
        if distance['distance'] >= max_distance:
            points[distance['name']] += 1
            max_distance = distance['distance']


ex_input = open('input.txt', 'r')

time = 2503
players = [get_cmd(line) for line in ex_input]
points = dict((player.name, 0) for player in players)
distances = dict((player.name, 0) for player in players)

for current_time in range(time):
    for player in players:
        time_in_cycle = current_time % player.get_cycle_time()
        if time_in_cycle < player.uptime:
            distances[player.name] += player.speed

    give_points(
        [{ 'name': key, 'distance': value } for key, value in distances.items()],
        points
    )

print points
