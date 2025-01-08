class Pizza:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)
        self.price += topping.price

    def __str__(self):
        toppings_str = ", ".join(topping.name for topping in self.toppings)
        return f"{self.size.capitalize()} {self.name} ({self.price} CZK) with toppings: {toppings_str}"