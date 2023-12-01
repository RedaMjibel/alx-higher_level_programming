#!/usr/bin/python3
# Finds a peak in a list of unsorted integers

def find_peak(list_of_integers):
    result = []
    for i in range(1, len(list_of_integers) - 1):
        if list_of_integers[i - 1] <= list_of_integers[i] >= list_of_integers[i + 1]:
            peak = list_of_integers[i]
            result.append(peak)
    if len(result) == 1:
        return peak
    elif len(result) == 0:
        return None
    else:
        return result
