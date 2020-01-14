cities = {
    'moscow' : {
        'country': 'russia',
        'population':'8 millions',
        'nationality':'russians',
    },
    'tokyo' : {
        'country':'japan',
        'population':'14 millions',
        'nationality':'japans',
    },
    'new york':{
        'country':'usa',
        'population':'20 millions',
        'nationality':'americans',
    },
}
for name, data in cities.items():
    print(f"\nДанные для города {name.title()}:")
    if data['country'] == 'usa':
        print(f"\tCountry: {data['country'].upper()}")
    else:
        print(f"\tCountry: {data['country'].title()}")
    print(str(f"\tPopulation: {data['population'].title()}"))
    print(f"\tNationality: {data['nationality'].title()}")