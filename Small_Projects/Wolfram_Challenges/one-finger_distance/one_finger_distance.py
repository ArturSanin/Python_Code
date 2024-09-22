"""
    Description: This is my attempted on the Wolfram Challenge One-Finger Distance, that you can find under the
    following link: https://challenges.wolframcloud.com/challenge/one-finger-distance
"""


def one_finger_distance(word):
    """

    :param word: A string only containing lowercase letters.
    :return: One finger distance of the word.
    """
    lowercase_letters = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
    word_length = len(word)
    distance = 0
    for character in word:
        if character not in lowercase_letters:
            raise ValueError("Your input must be a word consisting of small letters.")
    for i in range(word_length - 1):
        letter_index_1 = lowercase_letters.index(word[i])
        letter_index_2 = lowercase_letters.index(word[i + 1])
        absolut_value_index_differenz = abs(letter_index_2 - letter_index_1)
        if absolut_value_index_differenz <= 1:
            distance = distance + 0
        else:
            distance = distance + absolut_value_index_differenz - 1
    return distance
