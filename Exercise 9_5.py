class User:
    def __init__(self, first_name, last_name, age, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} {self.age} years old.")

    def greet_user(self):
        print(f"Welcome to our club MRs. {self.first_name} {self.last_name} with {self.login_attempts}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
new_user = User('Emil', 'Fattakhov', 29, 3)
new_user.describe_user()
new_user.greet_user()
new_user.increment_login_attempts()
new_user.greet_user()
new_user.reset_login_attempts()
new_user.greet_user()