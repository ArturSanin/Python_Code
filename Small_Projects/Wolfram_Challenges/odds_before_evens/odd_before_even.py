"""
    Description: This is my attempted on the Wolfram Challenge Odds before Evens, that you can find under the following
     link: https://challenges.wolfram.com/challenge/odds-before-evens
"""


def odd_before_even(list_of_integers):
    """

    :param list_of_integers: A list of integers (positive or negative).
    :return: List, where all odd integers come before the even integers.
    """

    def list_of_integers_check(some_list):
        """

        :param some_list: Some list.
        :return: Returns True if the list contains only integers, else False.
        """
        boolean = True
        for i in range(len(some_list)):
            boolean = boolean and isinstance(some_list[i], int)
        return boolean
    if not list_of_integers_check(list_of_integers):
        raise TypeError("Input list must contain only integers.")
    else:
        list_of_odd_integers = []
        list_of_even_integers = []
        for j in range(len(list_of_integers)):
            if list_of_integers[j] % 2 == 1:
                list_of_odd_integers.append(list_of_integers[j])
            else:
                list_of_even_integers.append(list_of_integers[j])
        for k in range(len(list_of_even_integers)):
            list_of_odd_integers.append(list_of_even_integers[k])
    return list_of_odd_integers
