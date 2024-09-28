"""
    Description: This is my attempted on the Wolfram Challenge Integers with Given Digit Sums, that you can find under
    the following link: https://challenges.wolframcloud.com/challenge/integers-with-given-digit-sums
"""


def find_with_given_digit_sum(s):
    """

    :param s: Positive integer.
    :return: List of integers below 1000, with digit sum equal s.
    """

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

    if not isinstance(s, int) or s <= 0:
        raise ValueError("First argument must be a positiv integer.")
    else:
        digit_sum_list = []
        for i in range(1, 1000):
            digit_list = get_digits(i)
            digit_sum = 0
            for digit in digit_list:
                digit_sum = digit_sum + digit
            if digit_sum == s:
                digit_sum_list.append(i)
            else:
                continue
    return digit_sum_list
