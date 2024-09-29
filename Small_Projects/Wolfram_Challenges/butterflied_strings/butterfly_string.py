"""
    Description: This is my attempted on the Wolfram Challenge Butterflied Strings, that you can find under the
    following link: https://challenges.wolframcloud.com/challenge/fizz-buzz
"""


def butterfly_string(string):
    """

    :param string: Some string.
    :return: Input string concatinated with the reverse of itself.
    Example:
        Hallo -> HalloollaH
        Tree -> TreeeerT
        Car -> CarraC
    """
    if not isinstance(string, str):
        raise ValueError("Argument must be a string.")
    string_length = len(string)
    for i in range(string_length):
        string = string + string[string_length - 1 - i]
    return string
