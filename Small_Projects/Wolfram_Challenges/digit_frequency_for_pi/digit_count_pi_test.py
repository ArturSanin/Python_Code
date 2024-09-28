from digit_count_pi import digit_count_pi


integer_list = [1, 10, 40]

for integer in integer_list:
    print(digit_count_pi(integer, mode="list"))
    print(digit_count_pi(integer, mode="print"))
    print("")
