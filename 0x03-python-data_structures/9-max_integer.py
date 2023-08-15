#!/usr/bin/python3
def max_integer(my_list=[]):
    max_ = my_list[0]
    if len(my_list) == 0:
        return None
    for i in range(len(my_list)):
        if max_ < my_list[i]:
            max_ = my_list[i]
    return max_
