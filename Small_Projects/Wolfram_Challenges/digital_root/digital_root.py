"""
    Description: This is my attempted on the Wolfram Challenge Digital Root, that you can find under the following link:
    https://challenges.wolframcloud.com/challenge/digital-root
"""


def digital_root(n):
    """

    :param n: Positive integer.
    :return: The digital root of n.
    """
    digital_root_of_n = n

    def get_digits(q):
        """

        :param q: Some positive integer.
        :return: A list of all digits (integers from 0 to 9) of q.
        Examples:
            12345 -> [5, 4, 3, 2, 1]
            50345 -> [5, 4, 3, 0, 5]
            19564 -> [4, 6, 5, 9, 1]
        """
        list_of_digits = []
        loop_number = q
        while loop_number > 0:
            list_of_digits.append(loop_number % 10)
            loop_number = (loop_number - loop_number % 10) // 10
        return list_of_digits
    if not isinstance(n, int):
        raise ValueError("Your input must be a positive integer.")
    elif not n >= 0:
        raise ValueError("Your input must be a positive integer.")
    else:
        while digital_root_of_n >= 10:
            digits = get_digits(digital_root_of_n)
            sum_of_digits = 0
            for i in range(len(digits)):
                sum_of_digits = sum_of_digits + digits[i]
            digital_root_of_n = sum_of_digits
        return digital_root_of_n
