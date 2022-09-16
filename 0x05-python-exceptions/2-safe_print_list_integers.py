#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end="")
            n += 1
        except TypeError:
            continue
        except ValueError:
            continue
        print()
        return n
