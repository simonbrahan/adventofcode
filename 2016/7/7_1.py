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


def has_abba(sequences):
    for sequence in sequences:
        if len(sequence) < 4:
            continue

        idx = 0
        while idx < len(sequence) - 3:
            candidate = sequence[idx:idx+4]

            if candidate == candidate[::-1] and len(set(candidate)) == 2:
                return True

            idx += 1

    return False


tls_support_count = 0

for line in open('input', 'r'):
    address = line.strip()
    body_sequences, hypernet_sequences = parse_address(address)

    if not has_abba(hypernet_sequences) and has_abba(body_sequences):
        tls_support_count += 1

print tls_support_count
