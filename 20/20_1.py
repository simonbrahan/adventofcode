searched_present_count = 80

num_things = 10

houses = [0] * num_things
for elf in range(1, num_things + 1):
    for house in range(elf, num_things + 1, elf):
        house_index = house - 1
        houses[house_index] += elf * 10

for house_address, num_presents in enumerate(houses):
    if num_presents >= searched_present_count:
        print house_address + 1
