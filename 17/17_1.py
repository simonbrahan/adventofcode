import itertools
ex_input = open('input.txt')

containers = [int(size) for size in ex_input]

count = 0
min_containers = 999
for container_count in range(1, len(containers) + 1):
    container_options = itertools.combinations(containers, container_count)
    for opts in container_options:
        if sum(opts) is 150:
            if len(opts) < min_containers:
                count = 1
                min_containers = len(opts)
            elif len(opts) is min_containers:
                count += 1

print count
