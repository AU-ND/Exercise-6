def intecheck(num):
    try:
        int(num)
    except(ValueError):
        return 0
        print("Wow I've had this code lying around forever, and that's not a number.")

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