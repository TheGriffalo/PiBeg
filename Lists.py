number_list = [3, 5, 6, -8, 156]

number = number_list[0]

number_list[2] = 3
number_list.append(34)

new_list = []

for number in number_list:
    new_list.append(number * 2)
    
print(new_list)