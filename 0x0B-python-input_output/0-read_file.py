#!/usr/bin/python3

'''opens and reads file'''


def read_file(filename=""):
    '''opening and reading contents in the file'''

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
