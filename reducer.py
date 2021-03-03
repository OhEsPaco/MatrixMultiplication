#!/usr/bin/env python

import sys

last_key = None
running_total = 0

for input_line in sys.stdin:
    input_line = input_line.strip()
    this_key, value = input_line.split("\t", 1)
    values = value.split(',')

    if last_key == this_key:
        running_total += int(values[0]) * int(values[1])
    else:
        if last_key:
            print("{}\t{}".format(last_key, running_total))
        running_total = int(values[0]) * int(values[1])
        last_key = this_key

print("{}\t{}".format(last_key, running_total))
