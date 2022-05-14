current_list = [1, 5, 6, 10, 30, 100]

new_list = []

for list in current_list:
    if list > 10:
        new_list.append(list)

print(new_list)