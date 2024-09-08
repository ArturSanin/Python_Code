"""
    Description: This is my attempted on the Wolfram Challenge Square Root Floor Digits, that you can find under
    the following link: https://challenges.wolframcloud.com/challenge/square-root-floor-digits
"""
import math as m


def square_root_floor(n):
    """

    :param n: Positive integer.
    :return: A list of integers, where the digits of every number up to n are replaced by the floor of the square root
    of that digit.
    """
    if not isinstance(n, int):
        raise ValueError("Your input must be a positive integer.")
    elif not n > 0:
        raise ValueError("Your input must be a positive integer.")
    else:
        result_list = []
        list_of_numbers_up_to_n = []
        for i in range(n):
            list_of_numbers_up_to_n.append(i + 1)
        for j in range(len(list_of_numbers_up_to_n)):
            if list_of_numbers_up_to_n[j] <= 9:
                result_list.append(m.floor(m.sqrt(list_of_numbers_up_to_n[j])))
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

                def digits_to_number(list_of_digits):
                    """

                    :param list_of_digits: A list of integers (from 0 to 9), that represent the digits
                    of the resulting number.
                    :return: Number having the elements of the list as digits.
                    Examples:
                        [1, 2, 3, 4] -> 4321
                        [2, 3, 5, 7] -> 7532
                        [1, 0, 1, 2, 3, 7] -> 732101
                    """
                    resulting_number = 0
                    for p in range(len(list_of_digits)):
                        resulting_number = resulting_number + list_of_digits[p] * (10 ** p)
                    return resulting_number
                old_digits = get_digits(list_of_numbers_up_to_n[j])
                new_digits = []
                for k in range(len(old_digits)):
                    new_digits.append(m.floor(m.sqrt(old_digits[k])))
                result_list.append(digits_to_number(new_digits))
        return result_list
