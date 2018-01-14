import re

def parse_particle(particle_id, line):
    nums = map(int, re.findall('[-\d]+', line))
    return {'id': particle_id, 'p': nums[0:3], 'v': nums[3:6], 'a': nums[6:9]}


def abs_sum(arr):
    return sum(abs(num) for num in arr)


particles = []
with open('input.txt') as input_file:
    for particle_id, line in enumerate(input_file):
        particle = parse_particle(particle_id, line)
        particles.append(particle)

for p in filter(lambda particle: abs_sum(particle['a']) is 1, particles):
    print p

sorted_particles = sorted(
    particles, 
    key = lambda p: (abs_sum(p['a']), abs_sum(p['v']), abs_sum(p['p']))
)
