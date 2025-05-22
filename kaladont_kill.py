#!/usr/bin/env python



with open("dicts/serb.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

with open("killers.txt", "r") as file:
    killers = [line.strip() for line in file.readlines()]

used = set()
valid = set()

for i in lines:
    if len(i) >= 3:
        valid.add(i)

while True:
    word = input("word: ").lower()
    if not word:
        continue

    k = set()
    for i in killers:
        if word.endswith(i[0:2]):
            print(f">> kill: {i}")
            k.add(i)

    if len(k) > 0:
        c = input("more? [y/N]: ")
        if c.lower() != "y":
            continue

    empty = True
    for i in valid:
        if i.startswith(word[-2:]) and i not in k:
            print(i)
            empty = False

    if empty:
        print(">> empty")
