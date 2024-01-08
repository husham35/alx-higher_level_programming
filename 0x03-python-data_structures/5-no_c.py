#!/usr/bin/python3
def no_c(my_string):
    without_c = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            without_c += i
    return without_c
