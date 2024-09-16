"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4   

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if any(list_one == list_two[i:i+len(list_one)] for i in range(len(list_two) - len(list_one) + 1)):
        #any() is a built-in function that returns True if any of the elements in the iterable are True
        #range(len(B) - len_A + 1) to not be out of bounds when extracting chunks
        #B[i:i+len_A] extracts chunks of the length of A and slides by one each time without taking the i+len(A) elt
        return SUBLIST
    if any(list_two == list_one[i:i+len(list_two)] for i in range(len(list_one) - len(list_two) + 1)):
        return SUPERLIST
    return UNEQUAL