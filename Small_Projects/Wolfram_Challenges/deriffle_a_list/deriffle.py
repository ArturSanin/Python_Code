"""
    Description: This is my attempted on the Wolfram Challenge Deriffle a List, that you can find under the following
    link: https://challenges.wolframcloud.com/challenge/deriffle-a-list
    Remark: Because Python lists start with an even index, the first list will contain all elements with an even index.
"""


def deriffle(some_list):
    """

    :param some_list:
    :return:
    """
    list_1 = []
    list_2 = []
    deriffle_list = []
    some_list_length = len(some_list)
    for i in range(some_list_length):
        if i % 2 == 0:
            list_1.append(some_list[i])
        else:
            list_2.append(some_list[i])
    deriffle_list.append(list_1)
    deriffle_list.append(list_2)
    return deriffle_list
