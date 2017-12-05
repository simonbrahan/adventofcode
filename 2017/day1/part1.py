with open('input.txt', 'r') as input_file:
    input = [int(num) for num in input_file.read().strip()]
    input.append(input[0])
    total = 0

    for idx, num in enumerate(input):
        try:
            next_num = input[idx+1]
        except:
            next_num = 0

        if next_num == num:
            total += num

print total
