#!/usr/bin/python3
"""log parsing"""
import sys
from collections import defaultdict


def print_stats(total_size, status_count):
    """The function prints the tottal size of
        line input and status code.
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_count.keys()):
        print("{}: {}".format(status_code, status_count[status_code]))


def parse_line(line):
    line_parts = line.split()
    if len(line_parts) != 10:
        return None
    ip_address = line_parts[0]
    date = line_parts[3][1:]
    request = line_parts[5]
    status_code = line_parts[8]
    file_size = line_parts[9]

    if not request.startswith("GET") or not request.endswith("HTTP/1.1"):
        return None
    return ip_address, status_code, int(file_size)


def main():
    total_size = 0
    status_counts = defaultdict(int)
    lines_processed = 0

    try:
        for line in sys.stdin:
            parsed_line = parse_line(line)
            if parsed_line is None:
                continue
            _, status_code, file_size = parsed_line
            total_size += file_size
            status_counts[status_code] += 1
            lines_processed += 1

            if lines_processed % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
