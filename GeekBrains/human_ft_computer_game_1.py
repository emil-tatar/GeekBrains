import random

upper_limit = [100]
lower_limit = [1]

while True:
    computer_number = random.randint(lower_limit[-1]+1, upper_limit[-1]-1)
    print(computer_number)
    human_answer = input(f'Введите больше, меньше или больше: ')
    if human_answer == '>':
        lower_limit.append(computer_number)
        print(lower_limit)
    elif human_answer == '<':
        upper_limit.append(computer_number)
        print(upper_limit)
    elif human_answer == '=':
        print(f'Победа!')
        break