#!/usr/bin/python3

'''

An addition function

'''


def add_integer(a, b=98):
    '''Addition of integers only'''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    addition = int(a) + int(b)
    return addition
