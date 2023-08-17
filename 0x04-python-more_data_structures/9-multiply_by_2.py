#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_cp = dict(a_dictionary)
    for i in dict_cp:
        dict_cp[i] = dict_cp[i] * 2
    return (dict_cp)
