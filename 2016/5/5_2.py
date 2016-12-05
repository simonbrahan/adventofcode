import hashlib

door_id = 'abbhdwsy'
idx = 0
password_chars = [ None, None, None, None, None, None, None, None ]

while not all(password_chars):
    m = hashlib.md5(door_id + str(idx))
    idx_hash = m.hexdigest()
    idx += 1

    if idx_hash[:5] != '00000':
        continue

    if idx_hash[5].isalpha():
        continue

    char_idx = int(idx_hash[5])

    if char_idx >= len(password_chars) or password_chars[char_idx] is not None:
        continue

    password_chars[char_idx] = idx_hash[6]


print ''.join(password_chars)
