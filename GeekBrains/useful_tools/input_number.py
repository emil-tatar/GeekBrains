def unlucky_number(number):
    if number != 13:
        return number**2
    else:
        raise ValueError('ValueError')

number = int(input('Input number: '))

try:
    result = unlucky_number(number)
except:
    print('This is unlucky number')
else:
    print(result)
