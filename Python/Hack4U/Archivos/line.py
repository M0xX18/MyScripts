#!/usr/bin/env python3

with open("/etc/hosts", "r") as f:

    for i, line in enumerate(f):
        if i < 2:
            print(line.strip())
