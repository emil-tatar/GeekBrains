# script to choice random number from list

from random import choice

def choice_number():
    numbers = []
    for i in range(1, 5):
        number = input(f'Input number_{i}: ')
        numbers.append(number)
    print(choice(numbers))
    print(numbers)
if __name__ == '__main__':
    choice_number()



