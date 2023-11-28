"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {} # an empty array
    for element in items:
        str_element = str(element)
        frequencies[str_element] = frequencies.get(str_element,0) +1 
    return frequencies



