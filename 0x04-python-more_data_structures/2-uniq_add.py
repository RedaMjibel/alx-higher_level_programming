#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    uniq = set()

    for numbers in my_list:
        if numbers not in uniq:
            uniq.add(numbers)
            total = total + numbers
    return (total)
