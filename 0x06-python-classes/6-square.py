#!/usr/bin/python3

"""Defines a square"""


class Square:
    """Defined a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializing the attributes
        Args: size - size of the square

        Raises:
        TypeError: if size is not type int
        ValueError: if size is less than zero
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            if not isinstance(value[0], int) or not isinstance(value[1], int) or len(value) != 2 or value[1] < 0 or value[0] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Defined object area

        Returns: area of the class square
        """
        return (self.__size ** 2)

    def my_print(self):
        """printing the square of a number using # """
        if self.__size == 0:
            print()
        else:
            for digit in range(self.__position[1]):
                print()
            margin = ' ' * self.__position[0]
            string = '#' * self.__size
            for num in range(self.__size):
                print(margin, string, sep='')
