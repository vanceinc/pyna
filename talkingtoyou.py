#!/usr/bin/env python3

print("Reading from a file")
with open("example.txt", "r") as f:
    txt = f.read()
    print(txt)
    if "cat" in txt:
        print("YEP!")
