def has_surrounded_letter(test_string):
    import re

    for char in test_string:
        pattern = re.compile('.*?' + char + '.' + char + '.*')

        if pattern.match(test_string):
            return True

    return False

def has_repeating_pair(test_string):
    for idx, char in enumerate(test_string):
        # Skip iteration for first character as we don't have a character pair yet
        if idx == 0:
            continue

        pair = test_string[idx - 1] + test_string[idx]

        # Look for pair after current pair
        if test_string.find(pair, idx + 1) > -1:
            return True

    return False

ex_input = open('5_input.txt', 'r')

for line in ex_input:
    line = line.strip()

    if not has_surrounded_letter(line):
        continue
    if not has_repeating_pair(line):
        continue

    print line
