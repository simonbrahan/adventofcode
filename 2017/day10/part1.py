from knothash import twist

def parse_input(filename):
    with open(filename) as input_file:
        return [int(val.strip()) for val in input_file.read().split(',')]


items = range(256)
instrs = parse_input('input.txt')
skip_size = 0
current_idx = 0

for twist_length in instrs:
    twist(items, current_idx, twist_length)
    current_idx += twist_length + skip_size
    skip_size += 1

print items

