def twist(items, start_idx, length):
    twist_idxs = [x % len(items) for x in range(start_idx, start_idx + length)]
    twist_vals = [items[idx] for idx in twist_idxs]
    twist_vals.reverse()

    for idx, items_idx in enumerate(twist_idxs):
        items[items_idx] = twist_vals[idx]


def hash(input):
    from operator import xor

    instrs = [ord(char) for char in input] + [17, 31, 73, 47, 23]
    sparse_hash = range(256)

    skip_size = 0
    current_idx = 0

    for i in range(64):
        for twist_length in instrs:
            twist(sparse_hash, current_idx, twist_length)
            current_idx += twist_length + skip_size
            skip_size += 1

    split_hash = [sparse_hash[i:i+16] for i in range(0, 255, 16)]
    dense_hash = map(lambda x: reduce(xor, x), split_hash)

    return ''.join(map(lambda num: hex(num)[2:].rjust(2, '0'), dense_hash)).rjust(32, '0')
