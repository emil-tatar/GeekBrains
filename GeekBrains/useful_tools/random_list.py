random_list = [1, -2, -34, 21, 342, -22, -4, -9, 75, 245, -69, 33, 17, 173, 0, 24]

if_list = [number for number in random_list if number%3 == 0 and number > 0 and number%4 != 0]
print(if_list)