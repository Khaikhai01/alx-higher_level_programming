#!/usr/bin/python3

'''class to json dictionary'''
import json


def class_to_json(obj):
    '''function to serialize obj'''
    dict = {}
    for key, value in obj.__dict__.items():
        dict[key] = value
    return dict
