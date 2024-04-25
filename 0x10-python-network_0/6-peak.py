#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    This approach usese a binary search.

    Args:
        list_of_integers (list): a list of unsorted integers

    Returns:
        int: the peak element in the list.
    """

    # check if list is not empty
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        # If the element to the right of mid is greater, search on the right
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        # If the element to the left of mid is greater, search on the left
        else:
            high = mid

    # At the end of the loop, low and high will converge to the peak element
    return list_of_integers[low]
