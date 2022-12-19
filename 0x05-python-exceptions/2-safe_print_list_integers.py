#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for num in range(x):
        try:
            print('{:d}'.format(my_list[num]), end='')
            counter += 1
        except (ValueError, TypeError):
            pass
    print()
    return counter
