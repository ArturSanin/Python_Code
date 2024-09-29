"""
    Description: This is my attempted on the Wolfram Challenge Replicate Characters in a String, that you can find under
    the following link: https://challenges.wolframcloud.com/challenge/replicate-characters-in-a-string
"""


def string_expand(some_string):
    """

    :param some_string: Some string.
    :return: A string where every letter is repeated according to the position of the letter in some_string.
    Example:
        a -> a
        ab -> abb
        abs -> abbccc
    """
    if not isinstance(some_string, str):
        raise ValueError("Argument must be a string.")
    output_string = ""
    i = 2
    for letter in some_string:
        for j in range(1, i):
            output_string = output_string + letter
        i += 1
    return output_string
