def parse_address(address):
    body_sequences = []
    hypernet_sequences = []
    current_sequence = ''
    in_hypernet_sequence = False

    for char in address:
        if char is '[':
            in_hypernet_sequence = True

            if len(current_sequence) > 0:
                body_sequences.append(current_sequence)
                current_sequence = ''

            continue

        if char is ']':
            in_hypernet_sequence = False

            if len(current_sequence) > 0:
                hypernet_sequences.append(current_sequence)
                current_sequence = ''

            continue

        current_sequence += char

    if len(current_sequence) > 0:
        body_sequences.append(current_sequence)

    return (body_sequences, hypernet_sequences)


def get_abas(sequences):
    output = []

    for sequence in sequences:
        if len(sequence) < 3:
            continue

        idx = 0
        while idx < len(sequence) - 2:
            candidate = sequence[idx:idx+3]

            if candidate == candidate[::-1] and len(set(candidate)) == 2:
                output.append(candidate)

            idx += 1

    return output


def supports_ssl(address):
    body_sequences, hypernet_sequences = parse_address(address)

    for body_aba in get_abas(body_sequences):
        for hypernet_aba in get_abas(hypernet_sequences):
            if set(body_aba) == set(hypernet_aba) and body_aba != hypernet_aba:
                return True

    return False


ssl_support_count = 0

for line in open('input', 'r'):
    if supports_ssl(line.strip()):
        ssl_support_count += 1

print ssl_support_count
