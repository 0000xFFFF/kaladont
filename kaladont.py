#!/usr/bin/env python

word = input("word: ")


with open("rs_fixed.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

used = set()
valid = set()

for i in lines:
    if len(i) >= 2:
        valid.add(i)

gameover = [
    "nt",
    "ih",
    "ry",
    "ao"
]

while True:

    if word[-2:] in gameover:
        print(">> game over.")
        exit(1)

    for i in valid:
        if i.startswith(word[-2:]) and i not in used:
            print(i)
            word = i
            used.add(i)
            continue

    break
