def twist(items, start_idx, length):
    twist_idxs = [x % len(items) for x in range(start_idx, start_idx + length)]
    twist_vals = [items[idx] for idx in twist_idxs]
    twist_vals.reverse()

    for idx, items_idx in enumerate(twist_idxs):
        items[items_idx] = twist_vals[idx]
