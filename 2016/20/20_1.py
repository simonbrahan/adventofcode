import datetime

def parse_range(range_str):
    return [ int(idx) for idx in range_str.split('-') ]


start_time = datetime.datetime.now()

blacklists = []
for line in open('input', 'r'):
    blacklists.append(parse_range(line.strip()))

blacklists.sort()

low_ip = 0

for blacklist_low, blacklist_high in blacklists:
    if low_ip < blacklist_low:
        break

    low_ip = blacklist_high + 1

print low_ip

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
