#!/usr/bin/python3
def search_replace(my_list, search, replace):

    if not my_list:
        return my_list

    temp_list = my_list.copy()
    for i, element in enumerate(temp_list, 0):
        if temp_list[i] == search:
            temp_list[i] = replace
    return temp_list
