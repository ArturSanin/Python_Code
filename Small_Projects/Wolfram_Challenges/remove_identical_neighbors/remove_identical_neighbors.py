"""
    Description: This is my attempted on the Wolfram Challenge Remove Identical Neighbors, that you can find under the
    following link: https://challenges.wolframcloud.com/challenge/remove-identical-neighbors
"""


def remove_identical_neighbors(some_list):
    """

    :param some_list: List.
    :return: List, with all list elements removed, that are equal to the element next to it.
    Example:
        [1, 1, 3, 4] -> [3, 4]
        [1, 1, 2, 3, 3] -> [2]
        [2, 2, 3, 3, 4, 4, 4, 4] -> []
    """
    list_with_neighbors_removed = []
    some_list_length = len(some_list)
    i = 0
    if some_list[some_list_length - 2] != some_list[some_list_length - 1]:
        while i <= some_list_length - 2:
            if some_list[i] == some_list[i + 1]:
                j = 1
                while some_list[i] == some_list[i + j]:
                    if i + j <= some_list_length - 2:
                        j += 1
                    else:
                        break
                i = i + j
            else:
                list_with_neighbors_removed.append(some_list[i])
                i += 1
        list_with_neighbors_removed.append(some_list[some_list_length - 1])
    else:
        while i <= some_list_length - 2:
            if some_list[i] == some_list[i + 1]:
                j = 1
                while some_list[i] == some_list[i + j]:
                    if i + j <= some_list_length - 2:
                        j += 1
                    else:
                        break
                i = i + j
            else:
                list_with_neighbors_removed.append(some_list[i])
                i += 1
    return list_with_neighbors_removed
