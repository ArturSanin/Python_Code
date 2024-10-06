"""
    Description: This is my attempted on the Wolfram Challenge Ascending Sublists, that you can find under the
    following link: https://challenges.wolfram.com/challenge/ascending-sublists
"""


def ascending_sublists(list_of_integers):
    """

    :param list_of_integers: A list of integers.
    :return: A list containing lists, where every sublist is ascending.
    """
    # Checking if the argument is a list.
    if not isinstance(list_of_integers, list):
        raise ValueError("Argument must be a list.")

    # Checking if the list contains only integers.
    boolean = False
    for element in list_of_integers:
        boolean = boolean or not isinstance(element, int)
    if boolean:
        raise ValueError("List must contain only integers.")

    # The following code finds all ascending sublists in list_of_integers.
    result_list = []  # In this list the ascending sublists will be stored.
    while 0 < len(list_of_integers):
        # This following loop creates the biggest sublist, where all sublist elements are ascending.
        sub_list = [list_of_integers[0]]
        list_of_integers.remove(list_of_integers[0])
        while 0 < len(list_of_integers):
            if sub_list[len(sub_list) - 1] >= list_of_integers[0]:
                break
            else:
                sub_list.append(list_of_integers[0])
                list_of_integers.remove(list_of_integers[0])

        # The sublist will only be included into the result list, when its length is bigger than 1.
        if len(sub_list) > 1:
            result_list.append(sub_list)

    return result_list
