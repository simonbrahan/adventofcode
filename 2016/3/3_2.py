current_batch = [[],[],[]]
possible_triangle_count = 0

for line in open('input', 'r'):
    line_sides = [
        int(side) for side in
            filter(None, line.strip().split(' '))
    ]

    for idx, length in enumerate(line_sides):
        current_batch[idx].append(length)


    if len(current_batch[0]) is 3:
        for sides in current_batch:
            sides.sort()

            if sides[0] + sides[1] > sides[2]:
                possible_triangle_count += 1


        current_batch = [[],[],[]]


print possible_triangle_count

