"""
    Description: This is my attempted on the Wolfram Challenge Pairs That Sum to 100, that you can find under the
    following link: https://challenges.wolframcloud.com/challenge/pairs-that-sum-to-100
"""


def pairs_add_to_hundred(list_of_integers):
    """

    :param list_of_integers: A list of integers.
    :return: A list containing pairs of numbers that sums up to 100.
    """
    list_of_pairs = []
    length_of_list = len(list_of_integers)
    i = 0
    while i < length_of_list:
        corresponding_value = 100 - list_of_integers[i]
        list_of_integers_value = list_of_integers[i]
        value_count = list_of_integers.count(list_of_integers_value)
        list_of_integers.remove(list_of_integers_value)
        if corresponding_value in list_of_integers:
            count = 0
            corresponding_value_count = list_of_integers.count(corresponding_value)
            product = value_count * corresponding_value_count
            min_value_of_pair = min(list_of_integers_value, corresponding_value)
            max_value_of_pair = max(list_of_integers_value, corresponding_value)
            for j in range(product):
                pair = (min_value_of_pair, max_value_of_pair)
                list_of_pairs.append(pair)
            for m in range(value_count - 1):
                list_of_integers.remove(list_of_integers_value)
                count += 1
            for n in range(corresponding_value_count):
                list_of_integers.remove(corresponding_value)
                count += 1
            length_of_list = length_of_list - (count + 1)
        else:
            length_of_list = length_of_list - 1
    return list_of_pairs
