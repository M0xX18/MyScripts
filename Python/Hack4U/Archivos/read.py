#!/usr/bin/env python3

with open("/etc/hosts", "r") as f:
    content = f.read()

print(content)
