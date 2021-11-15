class User:
    """Class of User"""
    def __init__(self, first_name, last_name, nickname, favorite_color, POLITICAL_ALIGNMENT, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.favorite_color = favorite_color
        self.POLITICAL_ALIGNMENT = POLITICAL_ALIGNMENT
        self.login_attempts = login_attempts

    def describe(self):
        print(f"This is {self.first_name.title()} {self.last_name.title()}, also known as {self.nickname}. Their favorite color is {self.favorite_color}, and they are a {self.POLITICAL_ALIGNMENT}.\nUser has logged in {self.login_attempts} times.")

    def greet_user(self):
        print(f"Hello {self.nickname}!")

    def login(self):
        self.greet_user()
        self.login_attempts = int(self.login_attempts) + 1
        print(f"You have logged in {self.login_attempts} times.")

    def loginreset(self):
        self.login_attempts = 0
        print("Login attempts reset.")