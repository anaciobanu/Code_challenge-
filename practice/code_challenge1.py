current_list = [1, 5, 6, 10, 30, 100, 101]

even_numbs = []
odd_numbs= []
#for i in current_list:
   # if i %5 == 0: new_list.append(i)


for i in range(31):
    if i %2 == 0:
        print(f'{i} is even')  
        even_numbs.append(i)
    else: 
        print(f'{i} is odd') 
        odd_numbs.append(i)  
print(even_numbs)
print(odd_numbs)