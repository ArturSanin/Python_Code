"""
    Description: This is my attempted on the Wolfram Challenge Square Sum, that you can find under the following link:
    https://challenges.wolframcloud.com/challenge/square-sum
"""


def square_sum(n):
    """

    :param n: Positive integer.
    :return: Iteratively summing and squaring the numbers 1 to n.
    """
    if not isinstance(n, int):
        raise ValueError("Your input must be a positive integer.")
    elif not n > 0:
        raise ValueError("Your input must be a positive integer.")
    else:
        result = 0
        for i in range(n + 1):
            result = (result + i) ** 2
        return result
