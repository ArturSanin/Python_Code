"""
    Description: This is my attempted on the Wolfram Challenge Number Triangles, that you can find under the following
    link: https://challenges.wolframcloud.com/challenge/number-triangles
"""


def number_triangle(n):
    """

    :param n: Positive integer.
    :return: Prints a sequence of lists of integers up to n.
    """
    if not isinstance(n, int):
        raise ValueError("Your input must be a positive integer.")
    elif not n >= 0:
        raise ValueError("Your input must be a positive integer.")
    else:
        for i in range(n - 1):
            list_variable = []
            for j in range(i + 1):
                list_variable.append(j + 1)
            print(list_variable)
        # Remark: The following list will be created, so this function can return something instead of None.
        last_list = []
        for k in range(n):
            last_list.append(k + 1)
        return last_list
