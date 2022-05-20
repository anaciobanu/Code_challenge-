names = ['Bob', 'Jennifer', 'Mike', 'Anna', 'Dell']
e_names = []
four_letter_names = []


for name in names:
    if 'e' in name:
        e_names.append(name)
        print(f'{name} has e ')
    if len(name) == 4:
        four_letter_names.append(name)
        print(f'{name} has 4 characters ')
    else:
        print(f'{name} not 4 characters')    
print(e_names)
print(four_letter_names)     