#!/usr/bin/python3

def uniq_add(my_list=[]):
    if not my_list:
        return my_list

    unique_items = set(my_list)
    return sum(unique_items)
