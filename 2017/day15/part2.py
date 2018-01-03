def generate_next(prev, factor, multiple):
    next_val = (prev * factor) % 2147483647
    if next_val % multiple is 0:
        return next_val
    else:
        return generate_next(next_val, factor, multiple)


def match(val_a, val_b):
    return val_a & 65535 == val_b & 65535


next_a = 679
next_b = 771

match_count = 0
for i in range(5000000):
    next_a = generate_next(next_a, 16807, 4)
    next_b = generate_next(next_b, 48271, 8)

    if match(next_a, next_b):
        match_count += 1

print match_count
