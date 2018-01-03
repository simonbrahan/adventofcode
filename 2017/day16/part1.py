from dancegroup import DanceGroup, do_dance

dg = DanceGroup('abcdefghijklmnop')

with open('input.txt') as input_file:
    do_dance(dg, input_file.read().strip().split(','))

print ''.join(dg.dancers)

