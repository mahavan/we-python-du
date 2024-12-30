class Pizza:
    def __init__(self, name, size, price, toppings=[]):
        self.name = name
        self.size = size
        self.price = price
        self.toppings = toppings

    def add_topping(self, topping):
        self.toppings.append(topping)
        self.price += topping.price
