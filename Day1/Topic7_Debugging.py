# Syntax error
#name = gaurav

# Runtime error
#a = 7
#b = a/0

# logical error
"""
def funcA(first_val, second_val):
    result = (first_val * 2) - (second_val / 0)
    return result


def functionB(first_val=23, last_val=72):
    # we would place our break point here
    response = funcA(first_val, last_val)
    result = response * first_val / 7
    return result

functionB(33, 88)
"""

# Using trace: https://www.codementor.io/gbozee/debugging-in-python-9ia7lof32
import pdb
def funcA(first_val, second_val):
    result = (first_val * 2) - (second_val / 0)
    return result


def functionB(first_val=23, last_val=72):
    # we would place our break point here
    response = funcA(first_val, last_val)
    result = response * first_val / 7
    return result

functionB(33, 88)