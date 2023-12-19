def count_uniques(list_of_strings):
    bookkeeping = {}
    for word in list_of_strings:
        if word not in bookkeeping:
            bookkeeping[word] = 1
        else:
            bookkeeping[word] += 1
    list_of_values = list(bookkeeping.values())
    return list_of_values


test_list = ["aa", "aa", "", "", "aa", "aa", "aa"]
print(count_uniques(test_list))