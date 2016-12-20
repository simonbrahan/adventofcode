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


start_time = datetime.datetime.now()

salt = 'ngcjuoqr'

idx = 0

candidates = []

for i in range(1000):
    candidates.append(md5.new(salt + str(i)).hexdigest())

keys = []
while len(keys) < 64:
    consider_hash = candidates.pop(0)
    hash_triple_char = find_triple(consider_hash)

    if hash_triple_char is not None and candidates_contain_quintuple(hash_triple_char):
        keys.append(consider_hash)

    candidates.append(md5.new(salt + str(1000 + idx)).hexdigest())
    idx += 1


print idx - 1

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
