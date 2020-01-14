class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is the kind of {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open now.")

restaurant_1 = Restaurant('romain', 'chill out')
restaurant_2 = Restaurant('marko polo', 'relax')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_2.describe_restaurant()