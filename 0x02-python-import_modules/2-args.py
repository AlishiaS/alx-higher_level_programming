#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)

    if n <= 1:
        print(0)
    else:
        if n == 2:
            print("{:d} argument:".format(n - 1))
        elif:
            print("{:d} arguments:".format(n - 1))

            for i in range(1, n):
                print("{:d}: {}".format(i, sys.argv[i]))