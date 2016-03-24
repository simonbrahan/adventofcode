def matching_house(houses, search_num_presents):
    for house_address, num_presents in enumerate(houses):
        if num_presents >= search_num_presents:
            return house_address + 1

searched_present_count = 33100000

num_things = 1600000

houses = [0] * num_things
for elf in range(1, num_things + 1):
    counter = 0
    for house in range(elf, num_things + 1, elf):
        counter += 1
        house_index = house - 1
        houses[house_index] += elf * 11
        if counter == 50:
            break

if max(houses) >= searched_present_count:
    print matching_house(houses, searched_present_count)
