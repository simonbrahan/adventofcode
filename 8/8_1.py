import re

ex_input = open('input.txt', 'r')

diff = 0

for line in ex_input:
    line = line.strip()
    line_char_length = len(line)
    print line
    print len(line)
    line = re.sub(r'(\\\\)|(\\")|(\\x[\da-fA-F]{2})', ' ', line)
    print line
    print len(line) - 2
    line_code_length = len(line) - 2
    diff += line_char_length - line_code_length

print diff
