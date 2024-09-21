from deriffle import deriffle


test_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_list_2 = []
test_list_3 = ['string']
test_list_4 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
test_list_5 = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWYZ']

print(deriffle(test_list_1))
print(deriffle(test_list_2))
print(deriffle(test_list_3))
print(deriffle(test_list_4))
print(deriffle(test_list_5))
