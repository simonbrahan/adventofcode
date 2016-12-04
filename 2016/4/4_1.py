def parse_room_str(room_str):
    import re

    pattern = re.compile('([a-z]+(-[a-z]+)*)-(\d+)\[([a-z]+)\]')
    res = re.search(pattern, room_str)

    return [ res.group(1), int(res.group(3)), res.group(4) ]


def get_checksum(name):
    letters_only = sorted([ char for char in name if char.isalpha()])
    letter_counts = dict( (letter, letters_only.count(letter)) for letter in set(letters_only))

    def order_items(item_a, item_b):
        if item_a[1] > item_b[1]:
            return -1

        if item_a[1] < item_b[1]:
            return 1

        if item_a[0] > item_b[0]:
            return 1
        else:
            return -1

    ordered_letters = [items[0] for items in sorted(letter_counts.items(), cmp=order_items)]

    return ''.join(ordered_letters[:5])


sector_sum = 0
for line in open('input', 'r'):
    line = line.strip()
    name, sector, checksum = parse_room_str(line)

    print line, get_checksum(name)

    if get_checksum(name) == checksum:
        sector_sum += sector

print sector_sum
