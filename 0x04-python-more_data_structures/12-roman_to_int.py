#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    if any(c not in numerals for c in roman_string):
        return 0

    rom_num = numerals[roman_string[0]]

    for i, s in enumerate(roman_string[1:], 1):
        if numerals[roman_string[i - 1]] < numerals[roman_string[i]]:
            rom_num += numerals[roman_string[i]] - 2 * (numerals[roman_string[i - 1]])
        else:
            rom_num += numerals[s]

    return rom_num
