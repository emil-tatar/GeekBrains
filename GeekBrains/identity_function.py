person = {
    'name': input(f'Введите имя: '),
    'age': int(input(f'Введите возраст')),
    'location': input(f'Введите город проживания: '),
}
def identity_function(person):
    print(f"{person['name']}, {person['age']} год(а), проживает в городе {person['location']} ")
    return

identity_function(person)