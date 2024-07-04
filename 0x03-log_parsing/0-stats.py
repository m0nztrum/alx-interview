#!/usr/bin/python3
"""Module reads from standard input and computes metrics"""

import sys


def process_input(line, cache, total_size, counter):
    """Process input line and update cache and total size"""
    line_list = line.split(" ")
    if len(line_list) > 4:
        code = line_list[-2]
        size = int(line_list[-1])
        if code in cache:
            cache[code] += 1
        total_size += size
        counter += 1
    return total_size, counter


def print_statistics(cache, total_size):
    """Print statistics"""
    print('File size:', total_size)
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


def main():
    """Main function to read from standard input and compute metrics"""
    cache = {'200': 0, '301': 0, '400': 0, '401': 0,
             '403': 0, '404': 0, '405': 0, '500': 0}
    total_size = 0
    counter = 0

    try:
        for line in sys.stdin:
            total_size, counter = process_input(line, cache,
                                                total_size, counter)
            if counter == 10:
                counter = 0
                print_statistics(cache, total_size)

    except KeyboardInterrupt:
        pass

    finally:
        print_statistics(cache, total_size)


if __name__ == "__main__":
    main()
