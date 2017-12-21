from scanners import parse_input, get_severity

scanners = parse_input(open('input.txt'))

print get_severity(scanners)
