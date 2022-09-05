#!/usr/bin/python3
def remove_char_at(str, n):
    x = 0
    newstr = ""

    for char in str:
        if x != str:
            newstr += char

        x += 1

    return newstr
