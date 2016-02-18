def contains_disallowed_strings(test_string):
    return any(bad_string in test_string for bad_string in ('ab', 'cd', 'pq', 'xy'))

def contains_enough_vowels(test_string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    vowel_count = 0

    for char in test_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count >= 3

def has_repeating_letters(test_string):
    last_char = ''

    for char in test_string:
        if char == last_char:
            return True
        last_char = char

    return False

ex_input = open('5_input.txt', 'r')

for line in ex_input:
    if contains_disallowed_strings(line):
        continue
    if not contains_enough_vowels(line):
        continue
    if has_repeating_letters(line):
        print line.strip()
