import sys
sys.path.append('../day10')
import knothash

def binary(hex_str):
    return str(bin(int(hex_str, 16)))[2:].rjust(128, '0')


def clean_region(grid, x, y):
    grid[y][x] = False
    if x > 0 and grid[y][x-1]:
        clean_region(grid, x-1, y)
    if x < 127 and grid[y][x+1]:
        clean_region(grid, x+1, y)
    if y > 0 and grid[y-1][x]:
        clean_region(grid, x, y-1)
    if y < 127 and grid[y+1][x]:
        clean_region(grid, x, y+1)


key = 'oundnydw'

grid = []
for i in range(128):
    hash = knothash.hash(key + '-' + str(i))
    grid.append([bit is '1' for bit in binary(hash)])

region_count = 0
for cell_y, line in enumerate(grid):
    for cell_x, cell in enumerate(line):
        if cell:
            region_count += 1
            clean_region(grid, cell_x, cell_y)

print region_count
