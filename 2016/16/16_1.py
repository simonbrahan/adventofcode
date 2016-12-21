import datetime

base = '10010000000110000'
disk_space = 272

def build_output(base, disk_space):
    output = base
    while len(output) < disk_space:
        next_section = output[::-1].replace('0', 't').replace('1', '0').replace('t', '1')
        output += '0' + next_section

    return output[:disk_space]


def build_checksum(data):
    output = data
    while len(output) % 2 == 0:
        idx = 0
        checksum = ''
        while idx < len(output) - 1:
            if output[idx] == output[idx + 1]:
                checksum += '1'
            else:
                checksum += '0'

            idx += 2

        output = checksum

    return output

start_time = datetime.datetime.now()

data = build_output(base, disk_space)

checksum = build_checksum(data)

print checksum

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
