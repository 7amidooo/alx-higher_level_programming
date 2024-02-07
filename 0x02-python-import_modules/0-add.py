#!/usr/bin/python3
'''
this is a program to print a + b in the direct mode only
'''
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
