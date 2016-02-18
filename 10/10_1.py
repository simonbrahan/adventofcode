input_sequence = '3113322113'

def get_section(sequence, start_at_index):
    considered_sequence = sequence[start_at_index:]
    if not len(considered_sequence):
        return ''

    start_char = considered_sequence[0]
    section = start_char
    for char in considered_sequence[1:]:
        if char is not start_char:
            return section

        section += start_char

    return section

def parse_section(section):
    return str(len(section)) + section[0]

for ignore in range(40):
    output_sequence = ''
    index = 0
    while True:
        section = get_section(input_sequence, index)

        if not len(section):
            break

        output_sequence += parse_section(section)
        index += len(section)

    input_sequence = output_sequence

print input_sequence
print len(input_sequence)
