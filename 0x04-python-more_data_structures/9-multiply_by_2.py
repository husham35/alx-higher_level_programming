#!/usr/bin/python3

def multiply_by_2(a_dictionary: dict):
    temp_dict = a_dictionary.copy()
    for key in temp_dict:
        temp_dict[key] = temp_dict[key] * 2

    return temp_dict
