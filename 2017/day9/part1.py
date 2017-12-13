stream = open('input.txt').read().strip()

group_score = 0
group_level = 0
in_garbage = False
is_escaped = False

for idx, char in enumerate(stream):
    if char is '!' and not is_escaped:
        is_escaped = True
        continue

    if char is '{' and not in_garbage:
        group_level += 1

    if char is '}' and not in_garbage:
        group_score += group_level
        group_level -= 1

    if char is '<' and not in_garbage:
        in_garbage = True

    if char is '>' and not is_escaped:
        in_garbage = False

    is_escaped = False


print group_score
