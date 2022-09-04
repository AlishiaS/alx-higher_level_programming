#!/usr/bin/python3
for num in range(10):
    for n in range(num + 1, 10):
        print("{}{}".format(num, n), end=", "
                if int(str(num) + str(n)) < 89 else "\n")
