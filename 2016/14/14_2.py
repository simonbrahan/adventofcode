import md5, datetime

def find_triple(input_str):
    idx = 0
    while idx < len(input_str) - 2:
        if input_str[idx] == input_str[idx + 1] == input_str[idx + 2]:
            return input_str[idx]

        idx += 1

    return None


def candidates_contain_quintuple(hash_triple_char):
    global candidates

    return any([ candidate for candidate in candidates if hash_triple_char * 5 in candidate ])


def create_hash(base):
    global salt

    output = salt + str(base)

    for i in range(2017):
        output = md5.new(output).hexdigest()

    return output


start_time = datetime.datetime.now()

salt = 'ngcjuoqr'

idx = 0

candidates = []

for i in range(1000):
    candidates.append(create_hash(i))

keys = []
while len(keys) < 64:
    consider_hash = candidates.pop(0)
    hash_triple_char = find_triple(consider_hash)

    if hash_triple_char is not None and candidates_contain_quintuple(hash_triple_char):
        keys.append(consider_hash)

    candidates.append(create_hash(1000 + idx))
    idx += 1

print idx - 1

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
