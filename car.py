def purchase_car(title, model, **car_info):
    print(f"You purchased car with following features: ")
    new_car = {}
    new_car['title_car'] = title
    new_car['model_car'] = model
    for key, value in car_info.items():
        new_car[key] = value
    return new_car
