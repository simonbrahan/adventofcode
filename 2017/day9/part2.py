stream = open('input.txt').read().strip()

in_garbage = False
is_escaped = False
garbage_count = 0

for char in stream:
    if is_escaped:
        is_escaped = False
        continue

    if char is '!' and not is_escaped:
        is_escaped = True
        continue

    if char is '>' and not is_escaped:
        in_garbage = False

    if in_garbage:
        garbage_count += 1

    if char is '<' and not in_garbage:
        in_garbage = True


print garbage_count
