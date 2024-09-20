"""
    Description: This is my attempted on the Wolfram Challenge Partitions of Increasing Length, that you
    can find under the following link: https://challenges.wolframcloud.com/challenge/partitions-of-increasing-length
"""


def partition_longer(some_list):
    """

    :param some_list: List.
    :return: A list of lists where every sublist is one element bigger then the sublist before.
    Example:
        [1, 2, 3, 4, 5, 6] -> [[1], [2, 3], [4, 5, 6]]
    """
    list_partition_longer = []
    partitions = []
    some_list_length = len(some_list)
    j = 0
    for i in range(some_list_length):
        j = j + i + 1
        if j <= some_list_length:
            partitions.append(i + 1)
        else:
            break
    partition_sum_lower = -1
    partition_sum_upper = 0
    for partition in partitions:
        partition_sum_upper = partition_sum_upper + partition
        help_list = []
        while partition_sum_lower + 1 <= partition_sum_upper - 1:
            help_list.append(some_list[partition_sum_lower + 1])
            partition_sum_lower += 1
        list_partition_longer.append(help_list)
        partition_sum_lower = partition_sum_upper - 1
    return list_partition_longer
