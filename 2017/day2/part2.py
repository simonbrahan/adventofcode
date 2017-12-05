def find_even_division(nums):
    """Given a list of integers,
       find the result of any even division.

       For example, given [2, 3, 4]
       return 2 (the even result of 4 / 2)
    """
    sorted_nums = sorted(nums)

    while sorted_nums != []:
        dividend = sorted_nums.pop()
        for divisor in sorted_nums:
            if dividend % divisor == 0:
                return dividend / divisor

    return False


with open('input.txt', 'r') as input_file:
    checksum = 0
    for line in input_file:
        parsed_line = [int(num) for num in line.split()]
        checksum += find_even_division(parsed_line)

print checksum
