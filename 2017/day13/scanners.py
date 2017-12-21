def parse_input(input_file):
    scanners = []

    for line in input_file:
        scanners.append([int(part) for part in line.split(': ')])

    return scanners


def get_severity(scanners):
    severity = 0

    for scan_depth, scan_range in scanners:
        if scan_depth % (scan_range * 2 - 2) is 0:
            severity += scan_depth * scan_range

    return severity
