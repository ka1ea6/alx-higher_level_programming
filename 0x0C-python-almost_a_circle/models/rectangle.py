#!/usr/bin/python3
'''Module for defining a Rectangle class'''

from models.base import Base


class Rectangle(Base):
    '''Class based on the Base class used for defining a Rectangle object'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Method to initialize an instance of rectangle based
        on the given values'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        '''Method to get the height of the rectangle instance'''

        return self.__height

    @height.setter
    def height(self, value):
        '''Method to set the value of the rectangle instance'''
        self.__check_type_int("height", value)
        self.__check_value("height", value, 1)
        self.__height = value

    @property
    def width(self):
        '''Method to get the height of the rectangle instance'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Method to set the value of the rectangle instance'''
        self.__check_type_int("width", value)
        self.__check_value("width", value, 1)
        self.__width = value

    @property
    def x(self):
        '''Method to get the height of the rectangle instance'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Method to set the value of the rectangle instance'''
        self.__check_type_int("x", value)
        self.__check_value("x", value, 0, message="must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Method to get the height of the rectangle instance'''

        return self.__y

    @y.setter
    def y(self, value):
        '''Method to set the value of the rectangle instance'''
        self.__check_type_int("y", value)
        self.__check_value("y", value, 0, message="must be >= 0")
        self.__y = value

    def __check_type_int(self, name, value, message="must be an integer"):
        '''Method to check if the passed value of the passed type'''
        if not isinstance(value, int):
            raise TypeError("{} {}".format(name, message))

    def __check_value(self, name, value, min, message="must be > 0"):
        '''Method to check if the values are greater than the min provided'''
        if isinstance(value, int) and value < min:
            raise ValueError("{} {}".format(name, message))

    def area(self):
        '''Method to return the area of the rectangle instance'''

        return self.height * self.width

    def display(self):
        '''Method to print the rectangle instance with '#' characters'''
        if self.y > 0:
            [print() for _ in range(self.y)]
        for _ in range(self.height):
            if self.x > 0:
                [print(' ', end="") for x in range(self.x)]
            [print('#', end="") for wid in range(self.width)]
            print()

    def update(self, *args, **kwargs):
        '''public method to assign an argument to the attributes'''
        for index, value in enumerate(args):
            self.__set_attribute(index, value)
        for key, val in kwargs.items():
            self.__set_attribute(key, val)

    def __set_attribute(self, key, value):
        '''Private method used as a helper to the update method'''
        if key == 0 or key == "id":
            self.id = value
            return
        elif key == 1 or key == "width" or key == "size":
            self.width = value
            return
        elif key == 2 or key == "height":
            self.height = value
            return
        elif key == 3 or key == "x":
            self.x = value
            return
        elif key == 4 or key == "y":
            self.y = value
            return

    def __str__(self):
        '''Dunder Method to return a stirng representing the object at hand'''
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}/{self.height}")

    def to_dictionary(self):
        '''Public method to return the dictionary
         representation of a Rectangle'''
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
