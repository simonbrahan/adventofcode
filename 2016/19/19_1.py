import datetime

num_elves = 3018458

start_time = datetime.datetime.now()

bin_format = '{0:b}'.format(num_elves)
rotated_bin_format = bin_format[1:] + bin_format[0]

print int(rotated_bin_format, 2)

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
