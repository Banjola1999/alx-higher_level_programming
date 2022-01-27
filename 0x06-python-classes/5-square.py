#!/usr/bin/python3
"""Class Square"""


class Square:
    """Getter and setter"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print('#', end="")
                print('')
