#!/usr/bin/python3

def uppercase(str):
    for alph in str:
        if ord(alph) >= 97 and ord(alph) <= 122:
            alph = chr(ord(alph) - 32)
        print("{:s}".format(alph), end='')

    print('\n', end="")
