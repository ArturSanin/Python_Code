"""
    Description: This is my attempted on the Wolfram Challenge Digit Frequency for Pi, that you can find under the
    following link: https://challenges.wolframcloud.com/challenge/constant-digit-sum
"""
from mpmath import *  # Python library for arbitrary-precision floating-point arithmetic.


def digit_count_pi(n, mode="list"):
    """

    :param n: Positive integer.
    :param mode: Return mode of the result. Only list or print possible. Default mode list.
    :return: List or print of the count of base 10 digits in the decimal expansion up to n places of pi.
    For list:
        index 0 -> Count of 0
        index 1 -> Count of 1
        index 2 -> Count of 2
        and so on.
    """
    modes = ["list", "print"]
    if not isinstance(n, int) or n <= 0:
        raise ValueError("First argument must be a positiv integers.")
    elif mode not in modes:
        raise ValueError("Your mode has to be list or print.")
    else:

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

        mp.dps = n  # Number of digits of pi.
        digit_count_pi_list = []
        pi_decimal_expansion_to_integer = int(mp.pi * 10 ** (n - 1))
        pi_decimal_expansion_to_integer_digits = get_digits(pi_decimal_expansion_to_integer)
        if mode == "list":
            for i in range(10):
                digit_count_pi_list.append(pi_decimal_expansion_to_integer_digits.count(i))
            return digit_count_pi_list
        elif mode == "print":
            for i in range(9):
                print(i, "Count:", pi_decimal_expansion_to_integer_digits.count(i))
            # Following return statement is for preventing the programm to return None in print mode.
            return str(9) + " Count: " + str(pi_decimal_expansion_to_integer_digits.count(9))
