import itertools
ex_input = open('input.txt')

containers = [int(size) for size in ex_input]

count = 0
for container_count in range(1, len(containers) + 1):
    container_options = itertools.combinations(containers, container_count)
    for opts in container_options:
        if sum(opts) is 150:
            count += 1

print count
