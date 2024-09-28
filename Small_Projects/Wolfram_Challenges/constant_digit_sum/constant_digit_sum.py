"""
    Description: This is my attempted on the Wolfram Challenge Constant Digit Sum, that you can find under the following
    link: https://challenges.wolframcloud.com/challenge/constant-digit-sum
"""


def constant_digit_sum(m, n, s):
    """

    :param m: Positiv integer.
    :param n: Positiv integer.
    :param s: Positiv integer.
    :return: List of integers from m to n with digit sum equal s.
    """
    constant_digit_sum_list = []

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

    if not isinstance(m, int) or m < 0:
        raise ValueError("First argument must be a positiv integer.")
    elif not isinstance(n, int) or n < 0:
        raise ValueError("Second argument must be a positiv integer.")
    elif not isinstance(s, int) or s < 0:
        raise ValueError("Third argument must be a positiv integer.")
    else:
        for i in range(m, n + 1):
            digit_list = get_digits(i)
            digit_sum = 0
            for j in digit_list:
                digit_sum = digit_sum + j
            if digit_sum == s:
                constant_digit_sum_list.append(i)
            else:
                continue
    return constant_digit_sum_list
