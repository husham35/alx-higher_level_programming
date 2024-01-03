#!/usr/bin/python3
for alph in range(97, 123):
    if chr(alph) == 'q' or chr(alph) == 'e':
        continue
    print(chr(alph).format(alph), end='')
