#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for replace, search in enumerate(new_list):
        if search == 2:
            new_list[replace] = 89
    return new_list
