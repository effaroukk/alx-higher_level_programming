#!/usr/bin/python3

"""Square class"""


class Square:
    """ Square class with size attribute"""
    def __init__(self, size=0):
        """
        Initializes Square class
        size: size of Square
        """
        self.__size = size

    @property  # getter
    def size(self):
        """
        Returns size of Square
        """
        return self.__size

    @size.setter  # setter
    def size(self, value):
        """
        Sets size of Square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns area of Square
        """
        return self.__size ** 2
