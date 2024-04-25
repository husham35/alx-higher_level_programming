#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): a list of unsorted integers

    Returns:
        int: the peak element in the list.
    """

    # check if list is not empty
    if not list_of_integers:
        return None

    # get length of the list 
    list_len = len(list_of_integers)
    # Get the middle index
    mid = (list_len // 2) - 1 if list_len % 2 == 0 else list_len // 2

    if list_len == 1:
        return list_of_integers[0]

    if list_len == 2:
        return max(list_of_integers)

    # If the middle element is larget than the next element, return it
    if (
        list_of_integers[mid - 1]
        <= list_of_integers[mid]
        >= list_of_integers[mid + 1]
    ):
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
