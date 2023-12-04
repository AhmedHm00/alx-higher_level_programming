#!/usr/bin/python3

"""
module for mylist class
"""

class MyList(list):
    """
    Provides sorted printing for the built-in list class.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        ."""
        print(sorted(self))
