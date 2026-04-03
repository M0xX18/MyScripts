#!/usr/bin/env python3

import re

text = "Katherine no me quiere pero ni un poquito, bueno de vez en cuando es que Katherine me quiere"

match = re.findall("Katherine", text)

print(match)
