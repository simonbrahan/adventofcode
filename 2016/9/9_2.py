def get_decompressed_size(compressed):
    import re
    next_marker = re.search('(\((\d+)x(\d+)\))', compressed)

    if next_marker:
        # Add input before next marker to output
        output = next_marker.start()

        # Get decompressed block size, multiply by number of repeats,
        # and add result to output
        char_count = int(next_marker.group(2))
        repeat_count = int(next_marker.group(3))
        repeat_block_start = next_marker.end()
        repeat_block_end = repeat_block_start + char_count
        repeat_block = compressed[repeat_block_start:repeat_block_end]
        decompressed_block_length = get_decompressed_size(repeat_block)
        output += decompressed_block_length * repeat_count

        # Continue parsing after found block
        return output + get_decompressed_size(compressed[repeat_block_end:])
    else:
        # No more markers - return input length
        return len(compressed)

input_str = open('input', 'r').read().strip()

print get_decompressed_size(input_str)
