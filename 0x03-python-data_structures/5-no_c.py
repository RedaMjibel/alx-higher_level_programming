#!/usr/bin/python3
def no_c(my_string):
    noc_string = ''.join(char for char in my_string if char not in ('c', 'C'))
    return (noc_string)
