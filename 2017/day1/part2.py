with open('input.txt', 'r') as input_file:
    input = [int(num) for num in input_file.read().strip()]
    input_length = len(input)
    input_midpoint = input_length / 2

    total = 0
    for idx, num in enumerate(input):
        matching_idx = (idx + input_midpoint) % input_length
        matching_num = input[matching_idx]

        if matching_num == num:
            total += num

print total
