"""
    Description: This is my attempted on the Wolfram Challenge Fizz Buzz, that you can find under the following link:
    https://challenges.wolframcloud.com/challenge/fizz-buzz
"""


def fizz_buzz(n):
    """

    :param n: Positive integer.
    :return: List from 1 to n, where every multiple of 3 is replaced by "fizz", every multiple of 5 replaced by "buzz"
    and every multiple of 3 and 5 replaced by "fizzbuzz".
    """
    integer_list = []
    if not isinstance(n, int):
        raise ValueError("Your input must be a positive integer.")
    elif not n >= 0:
        raise ValueError("Your input must be a positive integer.")
    else:
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                integer_list.append("fizzbuzz")
            elif i % 3 == 0:
                integer_list.append("fizz")
            elif i % 5 == 0:
                integer_list.append("buzz")
            else:
                integer_list.append(i)
        return integer_list
