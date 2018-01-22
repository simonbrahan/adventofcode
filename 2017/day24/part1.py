def bridge_strength(components):
    return sum(map(sum, components))


def fmt_bridge(components):
    return '--'.join(str(c[0]) + '/' + str(c[1]) for c in components)


def get_compatible_components(components, port_num):
    return [c for c in components if port_num in c]

with open('input.txt') as input_file:
    components = sorted(
        [tuple(sorted(map(int, line.strip().split('/')))) for line in input_file],
        key = lambda component: (component[0], component[1])
    )

open_port = 0
compatible_components = get_compatible_components(components, open_port)

print compatible_components

