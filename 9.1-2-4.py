def intecheck(num):
    try:
        int(num)
    except(ValueError):
        return 0

class Restaurant:
    """Restaurant Class"""
    def __init__(self, name, cuisine, number_served=0):
        """Write name et Attribute"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = number_served

    def describe(self):
        print(f"The restuarant {self.name.title()} serves {self.cuisine} food.\n{self.number_served} customers have been served.")

    def open(self):
        print(f"{self.name.title()} is open!")

    def increment_number_served(self):
        check = 0
        while check == 0:
            increment = input(f"How many people have been served at {self.name.title()} today?\n>")
            if intecheck(increment) != 0:
                self.number_served = int(self.number_served) + int(increment)
                check = 1
            else:
                print("That's not a number!")

olivegarden = Restaurant('olive garden', 'italian')

olivegarden.describe()

burgerking = Restaurant('Burger King', 'american')

cybergrill = Restaurant('Cyber Grill', 'Big Shot')

burgerking.describe()
cybergrill.describe()

cybergrill.increment_number_served()
cybergrill.describe()
cybergrill.increment_number_served()
cybergrill.describe()