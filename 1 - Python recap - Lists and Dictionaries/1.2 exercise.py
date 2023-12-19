def organizer(mixed_list):
    list1 = []
    list2 = []
    for word in mixed_list:
        if word[0] == "x" or word[0] == "X":
            list1.append(word)
            list1 = sorted(list1)
        else:
            list2.append(word)
            list2 = sorted(list2)
    return list1 + list2

mixed_list = ["mixture", "xxx", "automaton", "xavier", "aave", "111"]
print(organizer(mixed_list))