from collections import defaultdict
from math import sqrt, floor

def show_img(image):
    for line in image:
        print ''.join(line)


def count_lit_pixels(image):
    return sum(map(lambda row: sum(pixel is '#' for pixel in row), image))


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
    chunk_width = 2 if len(img[0]) % 2 is 0 else 3
    img_side = len(img[0])
    output = []
    for i in range(0, img_side, chunk_width):
        for j in range(0, img_side, chunk_width):
            chunk = []
            for k in range(chunk_width):
                chunk.append(tuple(img[i+k][j:j+chunk_width]))

            output.append(tuple(chunk))

    return output


def unchunk_img(chunks):
    chunk_width = len(chunks[0][0])
    img_side_chunks = sqrt(len(chunks))

    output = defaultdict(list)
    for chunk_id, chunk in enumerate(chunks):
        output_chunk_row = int(floor(chunk_id / float(img_side_chunks))) * chunk_width
        for chunk_row_id, chunk_row in enumerate(chunk):
            output_row =  output_chunk_row + chunk_row_id
            output[output_row] += list(chunk_row)

    return tuple(tuple(row) for row in output.values())


def expand_img(image, patterns):
    chunks = chunk_img(image)
    expanded_chunks = []

    def swap_on_pattern(chunk, patterns):
        for pattern in patterns:
            if chunk in pattern['match']:
                return pattern['out']

    return unchunk_img([swap_on_pattern(chunk, patterns) for chunk in chunks])


with open('input.txt') as input_file:
    patterns = [parse_line(line) for line in input_file]

image = (('.','#','.'),('.','.','#'),('#','#','#'))

for i in range(5):
    image = expand_img(image, patterns)

print count_lit_pixels(image), 'pixels are on'
