#!/usr/bin/python3
'''Module for defining a class representing a rectangle'''


class Rectangle:
    '''Class for defining a rectangle'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''
        Class used for instantiation of object

        Args :
            width (int) : width of the rectangle
            height (int) : height of the rectangle
        '''
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
                string += str(Rectangle.print_symbol) * self.__width
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
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an integer of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_2 if rect_1.area() < rect_2.area() else rect_1


    

        