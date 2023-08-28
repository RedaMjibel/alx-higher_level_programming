#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    for element in my_list:
        try:
            if i < x:
                print("{:d}".format(my_list[i]), end='')
                count = count + 1
        except (ValueError, TypeError):
            pass
        i = i + 1
    print()
    return (count)
