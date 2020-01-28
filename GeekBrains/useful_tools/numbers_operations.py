import math

old_list = [45, 33, -44, 3, 12, -6, -10, 45, 625, 225, 32, 90, -36]

def numbers_operation(input_list):
    new_list = [math.sqrt(number) if number > 0 else number for number in old_list]
    return new_list

print(numbers_operation(old_list))
print(old_list)