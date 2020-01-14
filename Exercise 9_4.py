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

restaurant_1 = Restaurant('romain', 'chill out')
restaurant_2 = Restaurant('marko polo', 'relax')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_2.describe_restaurant()
restaurant_1.clients_served()
restaurant_1.set_number_clients(34)
restaurant_1.clients_served()
restaurant_1.increment_number_clients(100)
restaurant_1.clients_served()