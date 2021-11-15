from dependant357891112 import *
class Access:
    """Priviledges Class"""
    def __init__(self, level, access = 'null'):
        self.level = level
        if level > 2:
            access = ['can ban users', 'can add and delete posts', 'can post memes']
        elif level > 1:
            access = ['can add and delete posts', 'can post memes']
        elif level > 0:
            access - ['can post memes']
        else: access = "can't do nothing"
        self.access = access

    def privy(self):
        print(f"User's priviledges makes it so that they can {self.access}")

    def escalate(self):
        if self.level <= 2:
            self.level = 3
            self.access = ['can ban users', 'can add and delete posts', 'can post memes']


class Admin(User):
    """Class of Admin"""
    def __init__(self, first_name, last_name, nickname, favorite_color, POLITICAL_ALIGNMENT, login_attempts = 0, level = 0):
        super().__init__(first_name, last_name, nickname, favorite_color, POLITICAL_ALIGNMENT, login_attempts = 0)
        self.level = level
        self.priviledges = Access(self.level)

    def describe2(self):
        print(f"This is {self.nickname}, an admin..")