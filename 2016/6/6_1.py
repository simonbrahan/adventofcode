columns = None

for line in open('input', 'r'):
    if not columns:
        columns = [ [] for i in range(len(line.strip())) ]

    for idx, char in enumerate(line.strip()):
        columns[idx].append(char)

output = ''
for column in columns:
    output += max(set(column), key=column.count)

print output
