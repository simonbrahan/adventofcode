def parseLine(line):
    import re
    [root, weight, _, children] = re.match(r'(\w+) \((\d+)\)( -> ([\w ,]*))?', line).groups()
    weight = int(weight)

    if children:
        children = [child.strip() for child in children.split(',')]
    else:
        children = []

    return [root, weight, children]


roots = []
children = []

with open('input.txt') as input_file:
    for line in input_file:
        [root, _, root_children] = parseLine(line)
        roots.append(root)
        children += root_children
    
    print set(roots) - set(children)
