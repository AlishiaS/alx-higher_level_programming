#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i= len(sys.argv) - 1

    if i== 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{:d} arguments".format(i))

    for i >= 1:
        i = 0
        for n in sys.argv:
            if i != 0:
                print("{}: {}".format(i, n))

            i += 1
