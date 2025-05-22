#!/usr/bin/env python

with open("dicts/serb.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

used = set()
valid = set()

for i in lines:
    if len(i) >= 3:
        valid.add(i)

while True:

    word = ""
    try:
        word = input("word: ").lower()
    except KeyboardInterrupt:
        print("\n\n")
        break
    if not word:
        continue

    for i in valid:
        if i.startswith(word[-2:]) and i not in used:
            print(i)
            word = i
            used.add(i)
            continue

    print(">> game over.")
