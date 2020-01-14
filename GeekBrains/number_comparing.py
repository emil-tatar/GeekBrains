numbers = []

def number_comparing():
    for i in range(3):
        number = int(input(f'Введите число: '))
        numbers.append(number)
        print(f'Наибольшее число: {max(numbers)}')

number_comparing()