"""
    Code description: The following program encrypts a text using the Caesar encryption.
"""


def caesar_cipher_encoder(text, shifting_parameter):
    """

    :param text: Some text, that contains only letters from the latin alphabet and some punctuation marks.
    :param shifting_parameter: The parameter with whom every letter is shifted. Punctuation marks are not effected.
    :return: Caesar encrypted text.
    """

    lowercase_letters = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]  # List containing all lowercase letters.
    uppercase_letters = [letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]  # List containing all uppercase letters.
    punctuation_marks = [punctuation for punctuation in ",;.:?!"]  # List containing punctuation marks.

    def letter_to_position(letter):
        """

        :param letter: Uppercase or lowercase Letter from the Latin alphabet.
        :return: Number between 0 and 25, representing the position in the list lowercase_letters, if the letter is
        lowercase, or in the list uppercase_letters, if the letter is uppercase.
        """
        if letter not in uppercase_letters and letter not in lowercase_letters:
            raise ValueError("Only uppercase or lowercase letters allowed.")
        elif letter in lowercase_letters:
            j = 0
            while lowercase_letters[j] != letter:
                j = j + 1
            return j
        elif letter in uppercase_letters:
            j = 0
            while uppercase_letters[j] != letter:
                j = j + 1
            return j

    def cyclic_addition(number, k):
        """

        :param number: Some integer.
        :param k: Some integer.
        :return: The sum of number and k modulo 26.
        """
        if number >= 26:
            return "Only numbers between 0 and 25"
        else:
            return (number + k) % 26

    def letter_encoded(letter, k):
        """

        :param letter: Letter from the latin alphabet.
        :param k: Shifting parameter.
        :return: Letter shifted by k.
        """
        if letter not in uppercase_letters and letter not in lowercase_letters:
            raise ValueError("Only uppercase or lowercase letters allowed.")
        elif letter in uppercase_letters:
            letter_position = letter_to_position(letter)
            letter_position_shifted = cyclic_addition(letter_position, k)
            encoded_letter = uppercase_letters[letter_position_shifted]
            return encoded_letter
        elif letter in lowercase_letters:
            letter_position = letter_to_position(letter)
            letter_position_shifted = cyclic_addition(letter_position, k)
            encoded_letter = lowercase_letters[letter_position_shifted]
            return encoded_letter

    length_text = len(text)
    encoded_text = ""
    for i in range(length_text):
        if text[i] == " ":
            encoded_text = encoded_text + " "
        elif text[i] not in uppercase_letters and text[i] not in lowercase_letters and text[i] not in punctuation_marks:
            raise ValueError("Your text contains characters that are not allowed.")
        elif text[i] in punctuation_marks:
            encoded_text = encoded_text + text[i]
        else:
            encoded_text = encoded_text + letter_encoded(text[i], shifting_parameter)
    return encoded_text
