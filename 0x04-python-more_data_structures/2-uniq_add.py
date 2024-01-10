#!/usr/bin/python3

def uniq_add(my_list=[]):
    if not my_list:
        return my_list

    unique_items =  set()
    for item in my_list:
        if isinstance(item, int):
            unique_items.add(item)
    return sum(unique_items)
