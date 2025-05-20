#!/usr/bin/env python

import sys


with open("dicts/serb.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

used = set()
valid = []

for i in lines:
    if len(i) >= 3:
        valid.append(i)

counter = 0
word = valid[counter]
killer = set()

for x in valid:

    found = False
    for y in valid:
        if y.startswith(x[-2:]):
            found = True
            break

    if not found:
        killer.add(x) 
        sys.stdout.write(f"{x}\n")
        sys.stdout.flush()

