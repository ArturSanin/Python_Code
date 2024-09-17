from remove_identical_neighbors import remove_identical_neighbors


test_list_1 = [1, 1, 1, 2, 2, 2]
test_list_2 = [1, 2, 3, 4, 5, 6]
test_list_3 = [3, 4, 2, 4, 2, 2, 1, 1]
test_list_4 = ['Word', 1, 2, 'word', 'word', 3, 4]
test_list_5 = ['Word', 'word', 'word', 'Word']
test_list_6 = ['Word', 'Word', 'Word', 'Word', 'Word', 'Word', 'Word']
test_list_7 = [[1, 2, 3], [-2, -3, 5], [-2, -3, 5], [1, 2, 3]]
test_list_8 = [1, [1, -3, 2.5], 'A', 'A', 'b', -7.3, -7.3, 'B']


print(remove_identical_neighbors(test_list_1))
print(remove_identical_neighbors(test_list_2))
print(remove_identical_neighbors(test_list_3))
print(remove_identical_neighbors(test_list_4))
print(remove_identical_neighbors(test_list_5))
print(remove_identical_neighbors(test_list_6))
print(remove_identical_neighbors(test_list_7))
print(remove_identical_neighbors(test_list_8))
