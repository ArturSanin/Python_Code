"""
    Description: This is my attempted on the Wolfram Challenge Digital Root, that you can find under the following link:
    https://challenges.wolframcloud.com/challenge/aliquot-sequence
    Remark: Code needs optimization. Only shows up to 30 terms of the aliquote sequence.
"""


def aliquote_sequence(n):
    """

    :param n: Positive integer.
    :return: List with the aliquote sequence of n up to 30 terms.
    """

    def proper_divisor(integer):
        """

        :param integer: Some integer.
        :return: Returns a list of all proper divisors of integer.
        """
        proper_divisors_list = []
        for i in range(integer - 1):
            if integer % (i + 1) == 0:
                proper_divisors_list.append(i + 1)
            else:
                continue
        return proper_divisors_list

    def proper_divisor_sum(integer):
        """

        :param integer: Some integer.
        :return: The sum of all proper divisors of integer.
        """
        proper_divisor_list = proper_divisor(integer)
        proper_divisor_list_length = len(proper_divisor_list)
        proper_divisor_sum_variable = 0
        for i in range(proper_divisor_list_length):
            proper_divisor_sum_variable = proper_divisor_sum_variable + proper_divisor_list[i]
        return proper_divisor_sum_variable

    if not isinstance(n, int):
        raise ValueError("Your input must be a positive integer.")
    elif not n >= 0:
        raise ValueError("Your input must be a positive integer.")
    elif n == 1:
        return []
    else:
        aliquote_sequence_list = [n]
        m = n
        while 1 < 2:
            aliquote_sequence_list_length = len(aliquote_sequence_list)
            proper_divisor_sum_v = proper_divisor_sum(m)
            if aliquote_sequence_list_length > 30:
                break
            elif m == proper_divisor_sum_v:
                break
            elif proper_divisor_sum_v == 1:
                break
            elif aliquote_sequence_list[aliquote_sequence_list_length - 2] == proper_divisor_sum_v:
                break
            else:
                aliquote_sequence_list.append(proper_divisor_sum_v)
                m = proper_divisor_sum_v
        return aliquote_sequence_list
