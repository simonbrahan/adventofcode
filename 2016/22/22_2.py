import datetime, re, collections

def parse_node(line):
    pattern = '\/dev\/grid\/node-x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T\s+\d+\%'
    match = re.match(pattern, line)
    if not match:
        print line
    return int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))


start_time = datetime.datetime.now()

nodes = collections.defaultdict(dict)
for line in open('input', 'r'):
    node_details = parse_node(line.strip())
    nodes[node_details[1]][node_details[0]] = node_details[2], node_details[3]

y = 0
while y < len(nodes):
    output = ''

    x = 0
    while x < len(nodes[y]):
        node = nodes[y][x]
        if node[0] > 100:
            output += '#'

        elif node[0] == 0:
            output += '_'
        else:
            output += '.'

        x += 1

    y += 1

    print output

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
