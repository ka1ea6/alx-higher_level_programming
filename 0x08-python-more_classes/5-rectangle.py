#!/usr/bin/python3
'''Module for defining a class representing a rectangle'''


class Rectangle:
    '''Class for defining a rectangle'''

    def __init__(self, width=0, height=0):
        '''
        Class used for instantiation of object

        Args :
            width (int) : width of the rectangle
            height (int) : height of the rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Getter for the private instance variable width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter for the private instance variable width

        Args:
            value (int) : width of the rectangle
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        '''
        Getter for the private instance variable height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter for the private instance variable height

        Args:
            value (int) : height of the rectangle
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
        return

    def area(self):
        '''
        Public method to return the rectangle area
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''
        Public method to return the rectangle perimeter
        '''
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        '''
        Public method to return the rectangle represented as #
        '''
        string = ""
        if not self.__width == 0 and not self.__height == 0:
            for i in range(self.__height):
                string += "#" * self.__width
                if i < self.__height - 1:
                    string += '\n'
        return string

    def __repr__(self):
        '''
        public method to return the representation of the object
        that can be evald to get a string
        '''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
