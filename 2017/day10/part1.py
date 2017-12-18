def parse_input(filename):
    with open(filename) as input_file:
        return [int(val.strip()) for val in input_file.read().split(',')]


def twist(items, start_idx, length):
    twist_idxs = [x % len(items) for x in range(start_idx, start_idx + length)]
    twist_vals = [items[idx] for idx in twist_idxs]
    twist_vals.reverse()

    for idx, items_idx in enumerate(twist_idxs):
        items[items_idx] = twist_vals[idx]


items = range(256)
instrs = parse_input('input.txt')
skip_size = 0
current_idx = 0

for twist_length in instrs:
    twist(items, current_idx, twist_length)
    current_idx += twist_length + skip_size
    skip_size += 1

print items

