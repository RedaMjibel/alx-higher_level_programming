#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M':1000 }
    total = 0
    prev = 0
    if roman_string == None or not isinstance(roman_string, str):
        return 0

    for num in reversed(roman_string):
        integer = roman_numerals[num]
        if integer <= prev:
            total = total - integer
            prev = integer
        elif integer >= prev:
            total = total + integer

    return total
