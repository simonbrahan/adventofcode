with open('input.txt', 'r') as input_file:
    checksum = 0
    for line in input_file:
        parsed_line = [int(num) for num in line.split()]
        checksum += max(parsed_line) - min(parsed_line)

print checksum
