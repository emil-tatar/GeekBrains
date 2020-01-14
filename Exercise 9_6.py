class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is the kind of {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open now.")

    def clients_served(self):
        print(f"We have {str(self.number_served)} clients today")

    def set_number_clients(self, amount):
        self.number_served = amount

    def increment_number_clients(self, difference):
        self.number_served += difference

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chilie', 'karamel']

    def describe_flavors(self):
        print('Following flavors are ready to order: ')
        for flavor in self.flavors:
            print(flavor.title())

restaurant_1 = IceCreamStand('romain', 'chill out')
restaurant_2 = Restaurant('marko polo', 'relax')
restaurant_1.describe_flavors()
