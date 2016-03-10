import re

input_lines = []
for line in open('input.txt'):
    input_lines.append(line.strip())

molecule = re.findall('[A-Z][^A-Z]*', input_lines.pop())

transforms = []
for line in input_lines:
    pattern = re.compile('(\w+) => (\w+)')
    res = re.search(pattern, line)
    if res:
        transforms.append({ 'from': res.group(1), 'to': res.group(2) })
