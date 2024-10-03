"""
    Description: This file contains functions used on strings.
"""
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"  # String containing all lowercase letters.
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # String containing all uppercase letters.
numbers = "0123456789"  # String containing all numbers.


def str_length(string):
    """

    :param string: Some string.
    :return: Integer representing the length of the string.
    """
    if not isinstance(string, str):
        raise ValueError("Argument must be a string.")
    length_counter = 0
    for char in string:
        length_counter += 1
    return length_counter


def check_substring(string, substring):
    """

    :param string:
    :param substring:
    :return: True if substring is part of string, else False.
    """
    string_length = str_length(string)
    substring_length = str_length(substring)
    length_difference = string_length - substring_length
    boolean = False
    if length_difference < 0:
        return False
    for i in range(length_difference + 1):
        boolean = boolean or (substring == string[i: substring_length + i])
    return boolean


def str_is_lowercase(string):
    """

    :param string: Some string.
    :return: True if string contains only lowercase letters, else False.
    """
    if not isinstance(string, str):
        raise ValueError("Argument must be a string.")
    string_length = str_length(string)
    boolean = True
    for i in range(string_length):
        boolean = boolean and not check_substring(uppercase_letters, string[i])
    return boolean


def str_is_uppercase(string):
    """

    :param string: Some string.
    :return: True if string contains only uppercase letters, else False.
    """
    if not isinstance(string, str):
        raise ValueError("Argument must be a string.")
    string_length = str_length(string)
    boolean = True
    for i in range(string_length):
        boolean = boolean and not check_substring(lowercase_letters, string[i])
    return boolean
