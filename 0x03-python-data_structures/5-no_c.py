#!/usr/bin/env python3
def no_c(my_string):
#    new_string = ''
#   for c in my_string:
#        if (c != 'C' and c != 'c'):
#            new_string = new_string + c
#    print(new_string)
    return my_string.translate({ord(i): '' for i in 'cC'})
