def sorted_merged_list(list1, list2):
    merged_list = list1 + list2
    #return sorted(merged_list)
    new_lst = []
    while len(merged_list) > 0:
        for x in merged_list:
            if x == min(merged_list):
                new_lst.append(x)
                merged_list.remove(x)
    return new_lst

list1 = [10, 20, 30, 40, 50]
list2 = [5, 7, 25, 55]

print(sorted_merged_list(list1, list2))