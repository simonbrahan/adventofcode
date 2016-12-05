import md5

door_id = 'abbhdwsy'
idx = 0
password = ''

while len(password) < 8:
    m = md5.new(door_id + str(idx))
    idx_hash = m.hexdigest()
    idx += 1

    if idx_hash[:5] == '00000':
        password += idx_hash[5]

print password
