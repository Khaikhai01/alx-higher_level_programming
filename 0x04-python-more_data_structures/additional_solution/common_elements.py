#!/usr/bin/python3
def common_elements(set_1, set_2):
    commonElem = [item for item in set_2 if item not in set_1]
    return commonElem
