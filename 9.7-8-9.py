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


class Admin:
    """Class of Admin"""
    def __init__(self, name, level):
        self.level = level
        self.priviledges = Access(self.level)

    def describe(self):
        print(f"This is ..")

admin1 = Admin('bruhman', 2)

admin1.describe()
admin1.priviledges.privy()

admin2 = Admin('bruhlad', 3)

admin2.describe()
admin2.priviledges.privy()

admin1.describe()
admin1.priviledges.privy()
admin1.priviledges.escalate()
admin1.priviledges.privy()