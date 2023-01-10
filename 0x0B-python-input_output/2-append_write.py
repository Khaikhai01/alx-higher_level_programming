#!/usr/bin/python3

'''opens file'''


def append_write(filename="", text=""):
    '''opens and appends to the file'''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
