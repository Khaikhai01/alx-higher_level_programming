#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = []

    for item in my_list:
        if item not in newlist:
            newlist.append(item)
    print(newlist)

    res = sum(newlist)
    return res
