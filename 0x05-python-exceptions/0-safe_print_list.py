#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for element in my_list:
        try:
            print("{}".format(element), end="")
            i = i + 1
            if x > 0 and i >= x:
                break
        except Exception as ex:
            return i
    print(" ")
    return i
