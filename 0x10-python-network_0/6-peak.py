#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):

    size = list_of_integers
    if size == []:
        return None
    total = len(loi)
    if total == 1:
        return size[0]
    elif total == 2:
        return max(size)
    middle = int(total / 2)
    peak = size[middle]
    if peak > size[middle - 1] and peak > size[middle + 1]:
        return peak
    elif peak < size[middle - 1]:
        return find_peak(size[:middle])
    else:
        return find_peak(size[middle + 1:])
