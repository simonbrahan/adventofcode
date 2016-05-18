import datetime

def get_next_point(point):
    point['row'] -= 1
    point['col'] += 1

    if point['row'] < 1:
        point['row'] = point['col']
        point['col'] = 1

code = 20151125
point = { 'row': 1, 'col': 1 }
target_point = { 'row': 2978, 'col': 3083 }

start_time = datetime.datetime.now()

while point != target_point:
    get_next_point(point)
    code = (code * 252533) % 33554393

print code
print 'Script took', datetime.datetime.now() - start_time
