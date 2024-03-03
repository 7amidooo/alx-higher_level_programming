#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    x = 0
    y = 0
    if 0 < len(tuple_a):
        x += tuple_a[0]

    if 0 < len(tuple_b):
        x += tuple_b[0]

    if 1 < len(tuple_a):
        y += tuple_a[1]

    if 1 < len(tuple_b):
        y += tuple_b[1]

    return (x, y)
