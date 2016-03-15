import re

def reduce_molecule(molecule, transforms):
    if molecule == ['e']:
        return

    transform_index = transforms.keys()
    transform_index.sort(key=len)
    transform_index.reverse()

    for transform in transform_index:
        for i in reversed(range(len(molecule) - len(transform) + 1)):
            if tuple(molecule[i:i+len(transform)]) == transform:
                transformed_molecule = molecule[:i] + [transforms[transform]] + molecule[i+len(transform):]

                print transformed_molecule
                return reduce_molecule(transformed_molecule, transforms)


input_lines = []
for line in open('input.txt'):
    input_lines.append(line.strip())

molecule = re.findall('[A-Z][a-z]*', input_lines.pop())

transforms = {}
for line in input_lines:
    pattern = re.compile('(\w+) => (\w+)')
    res = re.search(pattern, line)
    if res:
        transforms[tuple(re.findall('[A-Z][a-z]*', res.group(2)))] = res.group(1)

reduce_molecule(molecule, transforms)
