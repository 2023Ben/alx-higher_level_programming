#!/usr/bin/python3
"""Loookup module.
Contain a function that returns the list of 
available attribtes and methods of an object
"""

def lookup(obj):
    """Return a list and methods of available attributes and methods of an object"""
    return dir(obj)
