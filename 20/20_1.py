searched_present_count = 13

def visit_houses(searched_present_count, num_houses = 1, num_elves = 1):
    houses = []
    for house in range(1, num_houses + 1):
        houses.append(0)
        for elf in range(1, num_elves + 1):
            if house % elf is 0:
                houses[house - 1] += elf

    if searched_present_count not in houses:
        return visit_houses(searched_present_count, num_houses + 1, num_elves + 1)

    return houses.index(searched_present_count) + 1

print visit_houses(searched_present_count)
