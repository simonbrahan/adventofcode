with open('input.txt') as input_file:
    instrs = [int(line.strip()) for line in input_file]

steps = 0
current = 0
while current < len(instrs):
    current_instr = instrs[current]
    instrs[current] += 1
    current += current_instr
    steps += 1

print steps
