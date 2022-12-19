#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print('{:d}'.format(value))
        return True
    except (ValueError, TypeError):
#print('{} is not an integeir'.format(value))
        return False
