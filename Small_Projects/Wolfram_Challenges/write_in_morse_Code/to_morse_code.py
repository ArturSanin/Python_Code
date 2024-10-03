"""
    Description: This is my attempted on the Wolfram Challenge Write in Morse Code, that you can find under the
    following link: https://challenges.wolframcloud.com/challenge/write-in-morse-code
"""


def to_morse_code(text):
    """

    :param text: A string representing a text.
    :return: Text translated into Morse code.
    """
    if not isinstance(text, str):
        raise ValueError("Argument must be a string.")
    lowercase_letters = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]  # List containing all lowercase letters.
    uppercase_letters = [letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]  # List containing all uppercase letters.
    morse_alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                      "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                      "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--",
                      "--.."]  # List containing the morse alphabet.
    morse_text = ""
    for char in text:
        if char == " ":
            morse_text = morse_text + "/ "
        elif char in lowercase_letters:
            morse_text = morse_text + morse_alphabet[lowercase_letters.index(char)] + " "
        elif char in uppercase_letters:
            morse_text = morse_text + morse_alphabet[uppercase_letters.index(char)] + " "
        else:
            morse_text = morse_text + " " + char
    return morse_text
