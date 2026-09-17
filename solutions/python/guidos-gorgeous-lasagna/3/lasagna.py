"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes. 
"""



EXPECTED_BAKE_TIME = 40




def bake_time_remaining(elapsed_bake_time):
    """  bake_time_remaining for the elapsed_bake_time function"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    

    




def preparation_time_in_minutes (number_of_layers):
    """  preparation_time_in_minutes for the number_of_layers function"""
    return number_of_layers * 2





def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """  elapsed_time_in_minutes for the number_of_layers, elapsed_bake_time function"""
    return number_of_layers * 2 + elapsed_bake_time