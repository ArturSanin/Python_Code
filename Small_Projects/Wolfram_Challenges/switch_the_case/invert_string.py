"""
    Description: This is my attempted on the Wolfram Challenge Switch the Case, that you can find under the
    following link: https://challenges.wolframcloud.com/challenge/switch-the-case
"""


def invert_string(string):
    """

    :param string: A string.
    :return: Returns a string, with uppercase and lowercase inverted.
    """
    lowercase_letters = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]  # List containing all lowercase letters.
    uppercase_letters = [letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]  # List containing all uppercase letters.
    inverted_string = ""
    string_length = len(string)
    if not isinstance(string, str):
        raise ValueError("Input must be a string.")
    else:
        for i in range(string_length):
            if string[i] not in lowercase_letters and string[i] not in uppercase_letters:
                inverted_string = inverted_string + string[i]
            elif string[i] in lowercase_letters:
                inverted_string = inverted_string + uppercase_letters[lowercase_letters.index(string[i])]
            elif string[i] in uppercase_letters:
                inverted_string = inverted_string + lowercase_letters[uppercase_letters.index(string[i])]
        return inverted_string
