SMALL = 'small'
MEDIUM = 'medium'
LARGE = 'large'

class Pizza:
    """A pizza with a size and optional toppings."""

    def __init__(self, size):
        self.size = size
        self.toppings = []

    def getPrice(self):
        """Price of pizza depends on size and number of toppings."""
        if self.size == SMALL:
            price = 120 + 20 * len(self.toppings)
        elif self.size == MEDIUM:
            price = 200 + 20 * len(self.toppings)
        elif self.size == LARGE:
            price = 280 + 20 * len(self.toppings)
        else:
            raise ValueError("Unknown pizza size "+self.size)
        return price
    
    def addTopping(self, topping):
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)

