#!/usr/bin/python3

"""Defines a square"""


class Square:
    """Defined a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation of the sqaure class
        Args: size - size of the square
              position - x and y axis position
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2 or\
            type(position[0]) is not int or type(position[1]) is not int\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size

        Raises:
        TypeError: if size is not type int
        ValueError: if size is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if type(value) is not tuple or len(value) != 2\
            or not isinstance(value[0], int) or\
            not isinstance(value[1], int)\
                or value[1] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of\
                    2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Defined object area

        Returns: area of the class square
        """
        return (self.__size ** 2)

    def my_print(self):
        """Defined a printing method for a square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            margin = " " * self.__position[0]
            string = "#" * self.__size
            for i in range(self.__size):
                print(margin, string, sep="")
