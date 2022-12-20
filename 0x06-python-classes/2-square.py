#!/usr/bin/python3

"""class defination """


class Square:
    """Square class defined """
    def __init__(self, size=0):
        """Initialized class attributes"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size to be >= zero")
        else:
            self.__size = size
