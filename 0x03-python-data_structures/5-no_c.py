#!/usr/bin/python3
def no_c(my_string):
    newString = my_string({ord(i): None for i in 'cC'})

    return newString
    