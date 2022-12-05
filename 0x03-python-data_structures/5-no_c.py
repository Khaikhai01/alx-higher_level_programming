#!/usr/bin/env python3
def no_c(my_string):
     return my_string.translate({ord(i): '' for i in 'cC'})
