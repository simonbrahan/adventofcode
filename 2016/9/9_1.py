import re

input_str = open('input', 'r').read().strip()

input_str = 'A(2x2)BCD(2x2)EFG'

output = ''

idx = 0

while idx < len(input_str):
    print input_str[idx:]
    next_marker = re.search('(\((\d+)x(\d+)\))', input_str[idx:])

    if next_marker:
        # Add input before next marker to output
        output += input_str[idx:next_marker.start()]

        print next_marker.group()
        print output

        char_count = int(next_marker.group(2))
        repeat_count = int(next_marker.group(3))

        repeat_block_start = next_marker.end()
        repeat_block_end = repeat_block_start + char_count
        repeat_block = input_str[repeat_block_start:repeat_block_end]

        repeated_block = repeat_block * repeat_count

        output += repeated_block

        idx = repeat_block_end
    else:
        # No more markers - append remaining input to output
        output += input_str[idx:]
        break

print output
