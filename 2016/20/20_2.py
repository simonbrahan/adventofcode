import datetime

def parse_range(range_str):
    return [ int(idx) for idx in range_str.split('-') ]


start_time = datetime.datetime.now()

blacklists = []
for line in open('input', 'r'):
    blacklists.append(parse_range(line.strip()))

blacklists.sort()

num_allowed_ips = 0
prev_high = 0
for blacklist_low, blacklist_high in blacklists:
    if prev_high < blacklist_low:
        num_allowed_ips += blacklist_low - prev_high

    prev_high = max(prev_high, blacklist_high + 1)

print num_allowed_ips

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
