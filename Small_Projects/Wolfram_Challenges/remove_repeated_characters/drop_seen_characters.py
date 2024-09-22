"""
    Description: This is my attempted on the Wolfram Challenge Remove Repeated Characters, that you can find under the
    following link: https://challenges.wolframcloud.com/challenge/remove-repeated-characters
"""


def drop_seen_characters(string):
    """

    :param string: Some string.
    :return: String, with all instances of every character from string besides the first one removed.
    """
    string_dropped_characters = ""
    string_characters_list = [character for character in string]
    while len(string_characters_list) > 0:
        character = string_characters_list[0]
        string_dropped_characters = string_dropped_characters + character
        while character in string_characters_list:
            string_characters_list.remove(character)
    return string_dropped_characters
