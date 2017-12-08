with open('input.txt') as input_file:
    blocks = [int(block) for block in input_file.read().strip().split()]

print blocks

high_block = blocks.index(max(blocks))
print high_block
