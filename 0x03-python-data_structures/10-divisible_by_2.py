#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list = []
    for i in my_list:
        if i % 2 == 1:
            list.append(False)
        else:
            list.append(True)
    return list
