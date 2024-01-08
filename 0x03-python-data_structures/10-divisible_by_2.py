#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_divisible = []
    for n in my_list:
        if n % 2 == 0:
            is_divisible.append(True)
        else:
            is_divisible.append(False)
    return is_divisible
