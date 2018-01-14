import re

def parse_particle(line):
    nums = map(int, re.findall('[-\d]+', line))
    return {'p': nums[0:3], 'v': nums[3:6], 'a': nums[6:9]}


def purge_collisions(particles):
    


particles = {}
with open('input.txt') as input_file:
    for idx, line in enumerate(input_file):
        particles[idx] = parse_particle(line)

while True:
    purge_collisions(particles)
    accelarate(particles)
    move(particles)
    print len(particles), 'particles remaining'
