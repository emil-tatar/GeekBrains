player = {
    'name': input(f'Введите имя игрока: '),
    'health': 100,
    'damage': 50,
    'armor' : 1.2,
}
enemy = {
    'name': input(f'Введите имя игрока: '),
    'health': 100,
    'damage': 55,
    'armor' : 1.1,
}
def attack(person_1, person_2):
    person_1['health'] -= damage_correction(person_1, person_2)
    return

def damage_correction(person_1, person_2):
    return person_2['damage']/person_1['armor']

attack(enemy, player)

print(player)
print(enemy)
print('Value')
