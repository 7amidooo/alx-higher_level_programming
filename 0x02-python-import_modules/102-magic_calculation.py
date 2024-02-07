#!/usr/bin/python3
'''
dealing with bytecode
'''


def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        ans = add(a, b)
        for x in range(4, 6):
            ans = add(ans, x)
        return ans
    else:
        return (sub(a, b))
