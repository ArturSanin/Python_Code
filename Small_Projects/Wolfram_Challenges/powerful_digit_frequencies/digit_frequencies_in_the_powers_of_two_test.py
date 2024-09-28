from digit_frequencies_in_the_powers_of_two import digit_frequencies_in_the_powers_of_two


integer_list = [10, 100, 1000, 10000]
for integer in integer_list:
    print(digit_frequencies_in_the_powers_of_two(integer, mode="list"))
    print(digit_frequencies_in_the_powers_of_two(integer, mode="print"))
    print("")
