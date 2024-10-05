"""
    Description: This is my attempted on the Wolfram Challenge Palindrome from a Word, that you can find under the
    following link: https://challenges.wolframcloud.com/challenge/palindrome-from-a-word
"""


def palindromize(string):
    """

    :param string: Some word.
    :return:
    """
    if not isinstance(string, str):
        raise ValueError("Argument must be a string.")
    if " " in string:
        raise ValueError("Argument cannot have white spaces.")
    string_length = len(string)
    # Transforming the argument string, so only the first letter could be a capital letter.
    string = string[0] + string[1: string_length].lower()
    palindrome_string_left = ""
    palindrome_string_right = ""
    i = 0
    j = 0
    while i < string_length - j:
        if len(string[i: string_length - j]) == 1:
            palindrome_string_left = palindrome_string_left + string[i]
            i += 1
        elif string[i] == string[string_length - 1 - j]:
            palindrome_string_left = palindrome_string_left + string[i]
            palindrome_string_right = string[i].lower() + palindrome_string_right
            i += 1
            j += 1
        else:
            palindrome_string_left = palindrome_string_left + string[i]
            palindrome_string_right = string[i].lower() + palindrome_string_right
            i += 1
    return palindrome_string_left + palindrome_string_right
