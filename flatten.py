def flatten(super_list):
    final_list = []
    for sub_list in super_list: 
        final_list.extend(sub_list)
    return final_list

print(flatten([[1, 2], [3, 4], [5, 6]]))    