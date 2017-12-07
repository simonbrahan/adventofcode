def is_valid_password(password):
    words = [''.join(sorted(word)) for word in password.split()]

    return len(words) == len(set(words))


with open('input.txt') as input_file:
    output = [line for line in input_file if is_valid_password(line)] 

print len(output)
