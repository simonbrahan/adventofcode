import itertools

def show_img(image):
    for line in image:
        print ''.join(line)


def rotate_pattern(pattern):
    return tuple(tuple(row) for row in list(zip(*reversed(pattern))))


def flip_pattern(pattern):
    return tuple(reversed(pattern))


def get_pattern_options(pattern):
    # Rotate pattern
    output = [pattern]
    for i in range(3):
        output.append(rotate_pattern(output[-1]))

    # Flip pattern
    output.append(flip_pattern(pattern))
    for i in range(3):
        output.append(rotate_pattern(output[-1]))

    return set(output)


def parse_pattern(pattern_str):
    return tuple(tuple(list(part)) for part in pattern_str.split('/'))


def parse_line(line):
    match, out = line.strip().split(' => ')
    return {
        'match': get_pattern_options(parse_pattern(match)),
        'out': parse_pattern(out)
    }


def chunk_img(img):
    chunk_width = 3 if len(img[0][0]) % 3 is 0 else 2


with open('input.txt') as input_file:
    patterns = [parse_line(line) for line in input_file]

image = (('.','#','.'),('.','.','#'),('#','#','#'))

show_img(image)
for pattern in patterns:
    if image in pattern['match']:
        show_img(pattern['out'])
