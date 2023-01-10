#!/usr/bin/python3

'''adds items to a json file'''
import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
jsFile = 'add_item.json'
args = argv[1:]
try:
    my_list = load_from_json_file(jsFile)
except FileNotFoundError:
    save_to_json_file(args, 'add_item.json')
else:
    my_list.extend(argv[1:])
    save_to_json_file(my_list, jsFile)
