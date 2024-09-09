"""
    Description: This is my attempted on the Wolfram Challenge Factorial Zeros, that you can find under the following
    link: https://challenges.wolframcloud.com/challenge/factorial-zeros
"""


def factorial_zeros(n):
    """

    :param n: Positive integer.
    :return: Number of zeros at the end of n factorial.
    """
    def factorial(m):
        product = 1
        for i in range(m):
            product = product * (i + 1)
        return product

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
    zeros_count = 0
    digits_of_n_factorial = get_digits(factorial(n))
    j = 0
    while digits_of_n_factorial[j] == 0:
        zeros_count += 1
        j += 1
    return zeros_count
