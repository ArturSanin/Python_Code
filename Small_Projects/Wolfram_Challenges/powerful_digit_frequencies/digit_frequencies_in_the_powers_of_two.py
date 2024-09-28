"""
    Description: This is my attempted on the Wolfram Challenge Powerful Digit Frequencies, that you can find
    under the following link: https://challenges.wolframcloud.com/challenge/powerful-digit-frequencies
"""


def digit_frequencies_in_the_powers_of_two(n, mode="list"):
    """

    :param n: Positive integer.
    :param mode: Return mode of the result. Only list or print possible. Default mode list.
    :return: List or print of the count of base-10 digits in the decimal expansion up to n places of pi.
     For list:
        index 0 -> Count of 0
        index 1 -> Count of 1
        index 2 -> Count of 2
        and so on.
    """
    modes = ["list", "print"]
    if not isinstance(n, int) or n <= 0:
        raise ValueError("First argument must be a positiv integers.")
    elif mode not in modes:
        raise ValueError("Your mode has to be list or print.")
    else:

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

        digits_count_list = []
        digits_list = get_digits(2 ** n)
        if mode == "list":
            for i in range(10):
                digits_count_list.append(digits_list.count(i))
            return digits_count_list
        elif mode == "print":
            for i in range(9):
                print(i, "Count:", digits_list.count(i))
            # Following return statement is for preventing the programm to return None in print mode.
            return str(9) + " Count: " + str(digits_list.count(9))
