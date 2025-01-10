"""
    Project description: The following code generates a random password (as a string) with specific number of numbers,
    lowercase letters, uppercase letters and symbols in it.
"""
import secrets  # Module for generating cryptographically strong random numbers.


def password_generator(n_numbers=1, n_lowercase_letters=0, n_uppercase_letters=0, n_symbols=0):
    """

    :param n_numbers: Integer. Number of numbers in the generated password. Default 1.
    :param n_lowercase_letters: Integer. Number of lowercase letters in the generated password. Default 0.
    :param n_uppercase_letters: Integer. Number of uppercase letters in the generated password. Default 0.
    :param n_symbols: Integer. Number of symbols in the generated password. Default 0.
    :return: Random string with the specific number of characters in it.
    """
    numbers = "0123456789"  # String containing all numbers.
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"  # String containing all lowercase letters.
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # String containing all uppercase letters.
    symbols = "!#$%&()*+,_-./<=>?@[]{}|~"  # String containing symbols.
    password = ""

    def list_of_random_numbers(n, p):
        """

        :param n: Integer. Amount of desired random numbers.
        :param p: Integer. Upper limit for random numbers created.
        :return: List of length n containing random integers in the interval [0, p).
        """
        random_numbers = []
        i = 0
        while i < n:
            random_numbers.append(secrets.randbelow(p))
            i += 1
        return random_numbers

    def random_char_string(length, characters):
        """

        :param length: Integer. Desired length of the random string.
        :param characters: String. String of characters of which the random string will consist of.
        :return: String. Random string created out of the characters in characters.
        """
        char_list_length = len(characters)
        random_numbers = list_of_random_numbers(length, char_list_length)
        char_password = ""
        for i in random_numbers:
            char_password = char_password + characters[i]
        return char_password

    # Creating for every character typ (numbers, lowercase letters, uppercase letters, symbols) a random string
    # with specific length (n_numbers, n_lowercase_letters, n_uppercase_letters, n_symbols) and then concatenating into
    # an ordered password.
    random_numbers_string = random_char_string(n_numbers, numbers)
    random_lowercase_letters_string = random_char_string(n_lowercase_letters, lowercase_letters)
    random_uppercase_letters_string = random_char_string(n_uppercase_letters, uppercase_letters)
    random_symbols_string = random_char_string(n_symbols, symbols)
    ordered_password = (random_numbers_string + random_lowercase_letters_string
                        + random_uppercase_letters_string + random_symbols_string)
    ordered_password_length = len(ordered_password)

    # Following loop rearranges the order of the ordered password randomly to create a random password.
    j = 0
    while j < ordered_password_length:
        random_number = secrets.randbelow(ordered_password_length - j)
        password = password + ordered_password[random_number]
        ordered_password = ordered_password[:random_number] + ordered_password[random_number + 1:]
        j += 1
    return password


