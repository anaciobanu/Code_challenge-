from math import remainder


# print numbers from 3 to 35 if the number an be divided by 5 with no remainder
for number in range(5,36):
    if number %5 == 0:
        print(f' {number}')