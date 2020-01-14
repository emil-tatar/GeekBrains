import random
computer_number = random.randint(1, 100)
upper_limit = [100]
lower_limit = [1]
while computer_number:
    print(computer_number)
    human_answer = input('Введите меньше, больше или равно: ')
    if human_answer == '>':
        computer_number = random.randint(computer_number, upper_limit[-1])
        upper_limit.append(computer_number)
        print(upper_limit)
    elif human_answer == '<':
        computer_number = random.randint(lower_limit[-1], computer_number)
        lower_limit.append(computer_number)
        print(lower_limit)
    elif human_answer == '=':
        print('Победа')
        break

