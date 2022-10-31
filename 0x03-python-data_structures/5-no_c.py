#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string({ord(i): None for i in 'cC'})

    return new_str
    