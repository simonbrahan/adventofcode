import datetime

def get_next_elf(elf_idx):
    global elves
    next_elf_idx = (elf_idx + 1) % len(elves)
    return next_elf_idx


num_elves = 3018458

start_time = datetime.datetime.now()

elves = range(1, num_elves + 1)

elf_idx = 0
while len(elves) > 1:
    next_elf_idx = get_next_elf(elf_idx)
    elves.pop(next_elf_idx)

    if next_elf_idx == 0:
        elf_idx = 0
    else:
        elf_idx = get_next_elf(elf_idx)

print elves[0]

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
