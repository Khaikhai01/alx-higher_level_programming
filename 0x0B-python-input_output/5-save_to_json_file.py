#!/usr/bin/python3

'''opens, writes and save object to text file'''
import json


def save_to_json_file(my_obj, filename):
    '''opens, writes and save object to text file'''

    with open(filename, 'a', encoding='utf-8') as jsFile:
        return json.dump(my_obj, jsFile)
