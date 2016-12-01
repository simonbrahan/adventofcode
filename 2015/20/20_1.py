def matching_house(houses, search_num_presents):
    for house_address, num_presents in enumerate(houses):
        if num_presents >= search_num_presents:
            return house_address + 1

searched_present_count = 3310000

num_things = 1600000

houses = [0] * num_things
for elf in range(1, num_things + 1):
    for house in range(elf, num_things + 1, elf):
        house_index = house - 1
        houses[house_index] += elf

if max(houses) >= searched_present_count:
    print matching_house(houses, searched_present_count)
