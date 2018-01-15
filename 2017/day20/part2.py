import re
from collections import defaultdict

def parse_particle(idx, line):
    nums = map(int, re.findall('[-\d]+', line))
    return {'id': idx, 'p': nums[0:3], 'v': nums[3:6], 'a': nums[6:9]}


def purge_collisions(particles):
    stacked_particles = defaultdict(list)
    for p in particles.values():
        stacked_particles[tuple(p['p'])].append(p)

    for stack in stacked_particles.values():
        if len(stack) is 1:
            continue

        for p in stack:
            del particles[p['id']]


def accelerate(particles):
    for p in particles.values():
       p['v'] = [v + a for v, a in zip(p['v'], p['a'])]


def move(particles):
    for p in particles.values():
       p['p'] = [v + a for v, a in zip(p['p'], p['v'])]


particles = {}
with open('input.txt') as input_file:
    for line_num, line in enumerate(input_file):
        particles[line_num] = (parse_particle(line_num, line))

while True:
    purge_collisions(particles)
    accelerate(particles)
    move(particles)
    print len(particles), 'particles remaining'
