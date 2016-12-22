import datetime

num_elves = 3018458

start_time = datetime.datetime.now()

p = 1
while 3 * p <= num_elves:
    p *= 3

if num_elves == p:
    print num_elves
else:
  print num_elves - p + max(num_elves - 2 * p, 0)

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
