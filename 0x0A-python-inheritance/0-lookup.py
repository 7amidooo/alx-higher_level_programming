#!/usr/bin/python3
"""
Function to list items of the class
"""

if __name__ == "__main__":
    def lookup(obj):
        """
        Lookup(obj)
        return: List of obj attributes and methods
        """
        obj1 = obj()
        return obj1.__dir__()