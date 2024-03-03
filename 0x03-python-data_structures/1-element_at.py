#!/usr/bin/python3
# 1-element_at.py
def element_at(my_list, idx):
    """Return an element from list."""
    if idx < 0 or idx >= len(my_list):
        return "none"
    return (my_list[idx])
