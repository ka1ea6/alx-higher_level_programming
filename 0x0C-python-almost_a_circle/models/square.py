#!/usr/bin/python3
'''Module for defining a Square Class'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class for definging a square object'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Dunder method for instantiating an object'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Funciton to return a stirng representing the object at hand'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        '''public method for getting the size of the square'''
        return self.height

    @size.setter
    def size(self, value):
        '''public method for setting the size of the square'''
        self.width = value
        self.height = value

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
        elif key == 1 or key == "size":
            self.width = value
            return
        elif key == 2 or key == "x":
            self.x = value
            return
        elif key == 3 or key == "y":
            self.y = value
            return

    def to_dictionary(self):
        '''Public method to return the dictionary
         representation of a Rectangle'''
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y
        }
