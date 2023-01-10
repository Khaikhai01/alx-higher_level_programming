#!/usr/bin/python3

""""instantiates a class and converts its items
to json representation"""


class Student:
    """defines a student including a method to
    represent the class in json"""

    def __init__(self, first_name, last_name, age):
        """instantiates the class object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """converts class attributes to jason
        representation"""
        my_dict = {}
        for key, value in self.__dict__.items():
            my_dict[key] = value
        return my_dict
