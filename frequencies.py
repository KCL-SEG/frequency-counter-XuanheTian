"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {} # an empty array
    for element in items:
        str_element = str(element)
        if str_element in frequencies:
            frequencies[str_element] = frequencies.get(str_element,0) +1 
#dict[key] gives a value of the key ,  and we try to  use .get() to get the value of the element or key, 
#if we can't get the value, we assign it o by default
    # Your code goes here
    return frequencies



