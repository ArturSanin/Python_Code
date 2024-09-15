from odd_before_even import odd_before_even


test_list_1 = [-1, -9, -3, 5, 7, 9, 7, 2, 8, -2, -6, -10, -8]
test_list_2 = [1, 100, 2, 3, 3, 7, 4, 5]
test_list_3 = [2, 2, 22, 222, 1]
test_list_4 = [4, 43, 2, 2, 22, 2323, 1]
test_list_5 = [-1, 2, 8, -9, -2, -3, -6, -10, -8, 5, 7, 9, 7]
test_list_6 = []


print(odd_before_even(test_list_1))
print(odd_before_even(test_list_2))
print(odd_before_even(test_list_3))
print(odd_before_even(test_list_4))
print(odd_before_even(test_list_5))
print(odd_before_even(test_list_6))


error_test_1 = ["a", 2, 4, "R"]
error_test_2 = [1.3, 2.4, 3.6]
error_test_3 = [[1, 2, 3], [-1, -2, -3]]
error_test_4 = ["a", "A", "b", "B"]
error_test_5 = [1, [], [2], 3, 4]


# print(odd_before_even(error_test_1))
# print(odd_before_even(error_test_2))
# print(odd_before_even(error_test_3))
# print(odd_before_even(error_test_4))
# print(odd_before_even(error_test_5))
