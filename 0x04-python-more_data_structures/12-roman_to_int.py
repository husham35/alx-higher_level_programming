#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }

    if any(c not in nums for c in roman_string):
        return 0

    r_num = nums[roman_string[0]]
    for i, s in enumerate(roman_string[1:], 1):
        if nums[roman_string[i-1]] < nums[roman_string[i]]:
            r_num += nums[roman_string[i]] - 2*(nums[roman_string[i-1]])
        else:
            r_num += nums[s]

    return r_num
