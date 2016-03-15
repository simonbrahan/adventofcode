import re

input_lines = []
for line in open('input.txt'):
    input_lines.append(line.strip())

molecule = re.findall('[A-Z][a-z]*', input_lines.pop())

transforms = {}
for line in input_lines:
    pattern = re.compile('(\w+) => (\w+)')
    res = re.search(pattern, line)
    if res:
        if res.group(1) not in transforms:
            transforms[res.group(1)] = []

        transforms[res.group(1)].append(res.group(2))

transformed_molecules = {}
for index, atom in enumerate(molecule):
    if atom in transforms:
        for transform in transforms[atom]:
            new_molecule = list(molecule)
            new_molecule[index] = transform
            transformed_molecules[''.join(new_molecule)] = None

print len(transformed_molecules.keys())
