import numpy as np

def num_to_ord(input_num):
    """
    Converts a number to its ordinal form.
    """
    if input_num % 100 in [11, 12, 13]:
        return str(input_num) + 'th'
    else:
        return str(input_num) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(input_num % 10, 'th')