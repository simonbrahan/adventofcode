registers = { 'a': 0, 'b': 0 }

program = []

for line in open('input.txt'):
    line = line.strip()

    cmd = line[0: 3]
    if cmd == 'jmp':
        opts = { 'offset': int(line[4:]) }
    elif cmd in ['jie', 'jio']:
        opts = { 'reg': line[4], 'offset': int(line[7:]) }
    else:
        opts = { 'reg': line[4:] }

    program.append({ 'cmd': cmd, 'opts': opts })


line_num = 0

while line_num < len(program):
    parsed_line = program[line_num]

    if parsed_line['cmd'] == 'hlf':
        registers[parsed_line['opts']['reg']] = registers[parsed_line['opts']['reg']] / 2

    if parsed_line['cmd'] == 'tpl':
        registers[parsed_line['opts']['reg']] = registers[parsed_line['opts']['reg']] * 3

    if parsed_line['cmd'] == 'inc':
        registers[parsed_line['opts']['reg']] += 1

    if parsed_line['cmd'] == 'jmp':
        line_num += parsed_line['opts']['offset']
        continue

    if parsed_line['cmd'] == 'jie' and registers[parsed_line['opts']['reg']] % 2 == 0:
        line_num += parsed_line['opts']['offset']
        continue

    if parsed_line['cmd'] == 'jio' and registers[parsed_line['opts']['reg']] % 2 == 1:
        line_num += parsed_line['opts']['offset']
        continue

    line_num += 1

print registers
