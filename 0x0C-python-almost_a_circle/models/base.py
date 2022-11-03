#!/usr/bin/python3
'''Module for defining a Base class'''


import csv
import json


class Base:
    '''Class used as a Base for other classes'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Function for initializing an instance'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Static method to return a JSON string representation
         of list_dictionaries'''
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Class method to write the json string representation
         of list_objs to a file'''
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            new_list = []
            if isinstance(list_objs, list):
                for obj in list_objs:
                    new_dict = obj.__class__.to_dictionary(obj)
                    new_list.append(new_dict)
            f.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        '''Static method to return the list
         of the JSON string representation'''
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Class method to create an instance from a given dictionary'''
        newRect = cls(0, 0)
        # print("here", newRect)
        newRect.update(**dictionary)
        return newRect

    @classmethod
    def load_from_file(cls):
        '''Class method to load an instance from a file'''
        res = []
        instances = []
        with open(f"{cls.__name__}.json", "r", encoding="utf-8") as f:
            res = Base.from_json_string(f.readline())
        for curr in res:
            instances.append(cls.create(**curr))
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Class method to write the given list object to a csv file'''
        rect_header = ("id", "width", "height", "x", "y")
        square_header = ("id", "size", "x", "y")
        csv_body = []
        with open(f"{cls.__name__}.csv", mode='w', encoding="utf-8") as f:
            for obj in list_objs:
                new_dict = obj.__class__.to_dictionary(obj)
                csv_body.append(new_dict)
            if cls.__name__ == "Rectangle":
                writer = csv.DictWriter(f, fieldnames=rect_header,
                                        lineterminator="\n")
            elif cls.__name__ == "Square":
                writer = csv.DictWriter(f, fieldnames=square_header,
                                        lineterminator="\n")

            writer.writeheader()
            writer.writerows(csv_body)

    @classmethod
    def load_from_file_csv(cls):
        '''Class method to load the instance variables from a csv file'''
        instances = []
        with open(f"{cls.__name__}.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row = dict([a, int(x)] for a, x in row.items())
                instances.append(cls.create(**row))
        return instances
