#!/usr/bin/python3

"""checks if a class is a subclass"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass of
    a_class, othwerwise returns false"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
