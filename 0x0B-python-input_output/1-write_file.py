#!/usr/bin/python3

'''opens the file'''


def write_file(filename="", text=""):
    '''opens and writes to the file'''

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
