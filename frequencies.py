"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}  # Initialize an empty dictionary to hold the frequencies.
    for element in items:  # Iterate through each item in the input list.
        str_element = str(element)  # Convert the item to a string, ensuring keys are strings.
        frequencies[str_element] = frequencies.get(str_element, 0) + 1  # Increment the count for each item (key).
    return frequencies  # Return the dictionary containing the frequencies.




