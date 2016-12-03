possible_triangle_count = 0

for line in open('input', 'r'):
    sides = sorted(
        [
            int(side) for side in
                filter(None, line.strip().split(' '))
        ]
    )

    if sides[0] + sides[1] > sides[2]:
        possible_triangle_count += 1


print possible_triangle_count
