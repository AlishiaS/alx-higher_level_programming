#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv)
    s = 0
    for i in range(1, num):
        s += int(argv[i])
    print("{}".format(s))
