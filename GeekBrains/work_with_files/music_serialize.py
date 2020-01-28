import pickle
import json

my_favourite_singer = {
    'name': 'Zivert',
    'tracks': ['Life', 'Кредо'],
    'Albums': {'name': 'Vinyl #1', 'year': 2018},
}

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_singer, f)

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_singer, f)

print('Объект записан')

