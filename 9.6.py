class IceCreamShop:
    """Ice Cream Shop Class"""
    def __init__(self, name, flavors):
        self.name = name
        self.flavors = flavors

    def describe(self):
        print(f"{self.name} is an ice cream shop that sells {self.flavors} ice cream.")

Bruhsters = IceCreamShop('Bruhsters', 'Vanilla, Chocolate, and Bruh')

Bruhsters.describe()