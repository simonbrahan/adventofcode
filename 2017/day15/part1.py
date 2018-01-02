def generate_next(prev, factor):
    return (prev * factor) % 2147483647


def match(val_a, val_b):
    return val_a & 65535 == val_b & 65535


factor_a = 16807
next_a = 679

factor_b = 48271
next_b = 771

match_count = 0
for i in range(40000000):
    next_a = generate_next(next_a, factor_a)
    next_b = generate_next(next_b, factor_b)

    if match(next_a, next_b):
        match_count += 1

print match_count
