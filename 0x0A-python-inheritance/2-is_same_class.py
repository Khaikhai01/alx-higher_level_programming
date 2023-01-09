#!/usr/bin/python3

"""Function to check object instances"""


def is_same_class(obj, a_class):
    """defined a object instance checking function
    Args:
    obj- object to check
    a_class- class to check in
    Returns - True or false
    """
    return (type(obj) == a_class)
