import re

ex_input = open('input.txt', 'r')

diff = 0

for line in ex_input:
    line = line.strip()
    line_char_length = len(line)
    print line
    print len(line)
    line = line.replace('"', '  ')
    line = line.replace('\\', '\\\\')
    print line
    print len(line) + 2
    line_encoded_length = len(line) + 2
    diff += line_encoded_length - line_char_length

print diff
