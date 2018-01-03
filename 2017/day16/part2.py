from dancegroup import DanceGroup, do_dance

dg = DanceGroup('abcdefghijklmnop')
num_reps = 1000000000

with open('input.txt') as input_file:
    instrs = input_file.read().strip().split(',')
    seen = {}
    i = 0
    found_cycle = False

    while i < num_reps:
        do_dance(dg, instrs)
        if dg.lineup() in seen and not found_cycle:
            # If a cycle is encountered, skip forward until the cycle no longer fits then resume
            cycle_length = i - seen[dg.lineup()]
            i = num_reps - (num_reps % cycle_length)
            found_cycle = True
        else:
            seen[dg.lineup()] = i

        i += 1

print dg.lineup()

