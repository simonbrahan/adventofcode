def increment(string):
    # If the string is overflown, add another character
    if not len(string):
        return 'a'

    last_char = string[-1:]

    if last_char is 'z':
        return increment(string[:-1]) + 'a'
    else:
        return string[:-1] + chr(ord(last_char) + 1)


def find_repeating_letters(string, start_at_char):
    last_char = ''
    test_string = string[start_at_char:]

    for index, char in enumerate(test_string):
        if char == last_char:
            return index - 1
        last_char = char

    return False

def contains_two_pairs(string):
    repeat_index = find_repeating_letters(string, 0)

    if repeat_index is not False:
        return find_repeating_letters(string, repeat_index + 2) is not False

    return False


def contains_disallowed_chars(string):
    import re

    pattern = re.compile('.*[ilo].*')

    return pattern.match(string)


def contains_char_straight(string):
    max_index = len(string) - 3
    for i in range(max_index + 1):
        start_char = string[i]
        start_char_ord = ord(start_char)
        next_char_ord = ord(string[i+1])
        last_char_ord = ord(string[i+2])
        if next_char_ord is start_char_ord + 1 and last_char_ord is start_char_ord + 2:
            return True

    return False

password = 'hepxcrrq'

while True:
    password = increment(password)
    if (contains_two_pairs(password) and
      contains_char_straight(password) and
      not contains_disallowed_chars(password)):
        break

print password
