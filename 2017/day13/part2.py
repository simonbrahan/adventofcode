from scanners import parse_input, is_safe

scanners = parse_input(open('input.txt'))
delay = -1
safe = False

while not safe:
    delay += 1
    safe = is_safe(scanners, delay)

print delay
