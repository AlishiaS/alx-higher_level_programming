#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    a_dir = dir(hidden_4)
    for n in a_dir:
        if n[:2] != '__':
            print("{}".format(n))
