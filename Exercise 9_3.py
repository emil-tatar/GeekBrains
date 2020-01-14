class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} {self.age} years old.")

    def greet_user(self):
        print(f"Welcome to our club MRs. {self.first_name} {self.last_name}!")
new_user = User('Emil', 'Fattakhov', 29)
new_user.describe_user()
new_user.greet_user()