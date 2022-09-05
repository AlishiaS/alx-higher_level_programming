#!/usr/bin/python3
for c in range(122, 96, -1):
    j = c
    if c % 2 != 0:
        j = c - 32
    print("{}".format(chr(j)), end="")
