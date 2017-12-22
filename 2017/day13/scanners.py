def parse_input(input_file):
    scanners = []

    for line in input_file:
        scanners.append([int(part) for part in line.split(': ')])

    return scanners


def is_caught(scan_depth, scan_range, delay = 0):
    return (scan_depth + delay) % (scan_range * 2 - 2) is 0


def get_severity(scanners):
    severity = 0

    for scan_depth, scan_range in scanners:
        if is_caught(scan_depth, scan_range):
            severity += scan_depth * scan_range

    return severity


def is_safe(scanners, delay):
    for scan_depth, scan_range in scanners:
        if is_caught(scan_depth, scan_range, delay):
            return False

    return True
