#!/usr/bin/python3

'''function tha opens and reads file'''


def read_file(filename=""):
    '''opening and reading contents in the file'''

    with open('my_file_0.txt', encoding='utf-8') as f:
        print(f.read())
