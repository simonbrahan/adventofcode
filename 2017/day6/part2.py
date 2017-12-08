def get_cycle_count(banks):
    memo = set()
    cycles = 0
    while str(banks) not in memo:
        memo.add(str(banks))
        high_bank = banks.index(max(banks))
        high_block_count = banks[high_bank]
        banks[high_bank] = 0

        for block_num in range(high_block_count):
            banks[(high_bank + block_num + 1) % len(banks)] += 1

        cycles += 1

    return cycles, banks

with open('input.txt') as input_file:
    banks = [int(bank) for bank in input_file.read().strip().split()]

cycles_to_first_repeat, repeating_banks = get_cycle_count(banks)

cycles_to_second_repeat, repeating_banks = get_cycle_count(repeating_banks)

print cycles_to_second_repeat
