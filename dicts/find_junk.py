#!/usr/bin/env python3

invalid_chars = [
    "!",
    "#",
    "(",
    ")",
    ",",
    "-",
    ".",
    "/",
    "=",
    "`",
    "{",
    "}",
    "~",
    "7",
    "9",
]

with open("rs.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    for i in lines:
        for x in invalid_chars:
            if x in i:
                print(i)
                break

