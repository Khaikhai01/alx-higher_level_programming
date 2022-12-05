#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    len_list = len(my_list)
    for i in range(len_list):
        if (my_list[i] % 2) == 0:
            new_list.append(True)
        elif (my_list[i] % 2) != 0:
            new_list.append(False)

    return new_list
