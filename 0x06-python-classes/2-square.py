#!/usr/bin/python3

"""class defination """


class Square:
    """Square class defined """
    def __init__(self, size=0):
        """Initialized class attributes
        Args: size - size of the square

        Raises:
        TypeError: if size is not type int
        ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size to be >= zero")
        else:
            self.__size = size
