import time

def get_live_count(row, col, matrix):
    translations = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    live_count = 0
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])

    for trans_row, trans_col in translations:
        check_row = row + trans_row
        check_col = col + trans_col

        if 0 <= check_row < matrix_height and 0 <= check_col < matrix_width:
            neighbour_stat = matrix[check_row][check_col]
        else:
            neighbour_stat = '.'

        if neighbour_stat is '#':
            live_count += 1

    return live_count


def get_state(row, col, char, matrix):
    if row in (0, len(matrix) - 1) and col in (0, len(matrix[0]) - 1):
        return '#'

    adjacent_live = get_live_count(row, col, matrix)

    if char is '#':
        if adjacent_live in (2, 3):
            return '#'
        else:
            return '.'
    else:
        if adjacent_live is 3:
            return '#'
        else:
            return '.'


def print_matrix(matrix):
    for line in matrix:
        print ''.join(line)

    print ''


def get_on_count(matrix):
    count = 0

    for row in matrix:
        for light in row:
            if light is '#':
                count += 1

    return count

start = time.time()

old_matrix = [line.strip() for line in open('input.txt', 'r')]

print_matrix(old_matrix)

for step in range(100):
    new_matrix = []
    for row, line in enumerate(old_matrix):
        new_matrix.append([])
        for col, char in enumerate(line):
            new_matrix[row].append(get_state(row, col, char, old_matrix))

    old_matrix = new_matrix

print_matrix(new_matrix)

print get_on_count(new_matrix)
print time.time() - start, 'seconds elapsed'
